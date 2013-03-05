try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree

from pyngfm.service import Service, SystemService, UserService
from pyngfm.trigger import Trigger


OK = "OK"
FAIL = "FAIL"


class Message(object):
    def __init__(self, id=None, method=None, rfc_time=None, unix_time=None,
                 title=None, body=None, services= [], location = None):
        self.id = id
        self.method = method
        self.rfc_time = rfc_time
        self.unix_time = unix_time
        self.services = services
        self.set_title(title)
        self.set_body(body)
        self.set_location(location)

    def set_id(self, id):
        self.id = id

    def set_method(self, method):
        self.method = method

    def set_rfc_time(self, rfc_time):
        self.rfc_time = rfc_time

    def set_unix_time(self, unix_time):
        self.unix_time = unix_time

    def set_title(self, title):
        if title:
            title = title.decode("base64")
        self.title = title

    def set_body(self, body):
        if body:
            body = body.decode("base64")
        self.body = body

    def add_service(self, service_id, service_name):
        service = {"id": service_id, "name": service_name}
        self.services.append(service)

    def set_location(self, location):
        if location:
            location = location.decode("base64")
        self.location = location


class Response(object):
    """
    A wrapper for the parsed respones from the ping.fm service.
    """
    def __init__(self, response):
        self.original = response
        self.element = ElementTree.XML(response)
        self.status = self.element.get("status")
        self.transaction = self.element.findtext("transaction")
        self.method = self.element.findtext("method")

    def get_key(self):
        return self.element.findtext("key")

    def get_message(self):
        return self.element.find("message").text

    def _parse_service_methods(self, methods):
        return [method.strip() for method in methods.split(",")]

    def get_services(self):
        services = []
        if self.method == "user.services":
            service_class = UserService
        elif self.method == "system.services":
            service_class = SystemService
        for service in self.element.find("services"):
            id = service.get("id")
            name = service.get("name")
            trigger = service.findtext("trigger")
            url = service.findtext("url")
            icon = service.findtext("icon")
            methods = service.findtext("methods")
            service_instance = service_class(id=id, name=name, trigger=trigger,
                                             url=url, icon=icon)
            if methods:
                service_instance.set_methods(
                    self._parse_service_methods(methods))
            services.append(service_instance)
        return services

    def get_triggers(self):
        triggers = []
        for trigger in self.element.find("triggers"):
            id = trigger.get("id")
            method = trigger.get("method")
            services = []
            for service in trigger.find("services"):
                service_id = service.get("id")
                service_name = service.get("name")
                service_instance = Service(id=service_id, name=service_name)
                services.append(service_instance)
            trigger_instance = Trigger(id=id, method=method, services=services)
            triggers.append(trigger_instance)
        return triggers

    def get_latest_messages(self):
        messages = []
        for message in self.element.find("messages"):
            id = message.get("id")
            method = message.get("method")
            rfc_time = message.find("date").get("rfc")
            unix_time = message.find("date").get("unix")
            title = message.find("content").findtext("title")
            body = message.find("content").findtext("body")
            location = message.findtext("location")
            services = []
            for service in message.find("services"):
                service_id = service.get("id")
                service_name = service.get("name")
                service_instance = Service(id=service_id, name=service_name)
                services.append(service_instance)
            message_instance = Message(
                id=id, method=method, rfc_time=rfc_time, unix_time=unix_time,
                title=title, body=body, location=location, services=services)
            messages.append(message_instance)
        return messages
