from twisted.trial.unittest import TestCase

from pyngfm.message import Message, Response, OK
from pyngfm.service import Service, SystemService, UserService
from pyngfm.testing import payload


class MessageTestCase(TestCase):

    def test_creation(self):
        services = [
            Service(id="id1", name="name1"),
            Service(id="id2", name="name2")]
        message = Message(id="id3", method="a.method", rfc_time="time1",
                          unix_time="time2", title="dGl0bGU=", body="Ym9keQ==",
                          services=services, location="dGhpcyBzcG90")
        self.assertEquals(message.id, "id3")
        self.assertEquals(message.method, "a.method")
        self.assertEquals(message.rfc_time, "time1")
        self.assertEquals(message.unix_time, "time2")
        self.assertEquals(message.title, "title")
        self.assertEquals(message.body, "body")
        self.assertEquals(message.location, "this spot")
        self.assertEquals(message.services[0].id, "id1")
        self.assertEquals(message.services[0].name, "name1")
        self.assertEquals(message.services[1].id, "id2")
        self.assertEquals(message.services[1].name, "name2")

class ResponseTestCase(TestCase):

    def test_creation(self):
        response = Response(payload.sample_response_ok)
        self.assertEquals(response.original, payload.sample_response_ok)
        self.assertEquals(response.element.tag, "rsp")
        self.assertEquals(response.status, OK)
        self.assertEquals(response.transaction, "12345")
        self.assertEquals(response.method, "user.services")

    def test_get_key(self):
        response = Response(payload.sample_user_key_ok)
        self.assertEquals(
            response.get_key(),
            "abcdeasdadsdghasdfaslkdjfa012345-1234567890")

    def test_get_message(self):
        response = Response(payload.sample_response_fail)
        self.assertEquals(
            response.get_message(),
            "User application key could not be validated.")

    def test_get_services_system(self):
        response = Response(payload.sample_system_services_ok)
        service1, service2 = response.get_services()

        self.assertTrue(isinstance(service1, SystemService))
        self.assertEquals(service1.id, "bebo")
        self.assertEquals(service1.name, "Bebo")
        self.assertEquals(service1.trigger, "@be")
        self.assertEquals(service1.url, "http://www.bebo.com/")
        self.assertEquals(
            service1.icon,
            "http://p.ping.fm/static/icons/bebo.png")

        self.assertTrue(isinstance(service2, SystemService))
        self.assertEquals(service2.id, "blogger")
        self.assertEquals(service2.name, "Blogger")
        self.assertEquals(service2.trigger, "@bl")
        self.assertEquals(service2.url, "http://www.blogger.com/")
        self.assertEquals(
            service2.icon,
            "http://p.ping.fm/static/icons/blogger.png")

    def test_parse_service_methods(self):
        response = Response(payload.sample_user_services_ok)
        methods = response._parse_service_methods("a,b,c")
        self.assertEquals(methods, ["a", "b", "c"])
        methods = response._parse_service_methods(" a , b , c ")
        self.assertEquals(methods, ["a", "b", "c"])

    def test_get_services_user(self):
        response = Response(payload.sample_user_services_ok)
        service1, service2 = response.get_services()

        self.assertTrue(isinstance(service1, UserService))
        self.assertEquals(service1.id, "twitter")
        self.assertEquals(service1.name, "Twitter")
        self.assertEquals(service1.trigger, "@tt")
        self.assertEquals(service1.url, "http://twitter.com/")
        self.assertEquals(
            service1.icon,
            "http://p.ping.fm/static/icons/twitter.png")

        self.assertTrue(isinstance(service2, UserService))
        self.assertEquals(service2.id, "facebook")
        self.assertEquals(service2.name, "Facebook")
        self.assertEquals(service2.trigger, "@fb")
        self.assertEquals(service2.url, "http://www.facebook.com/")
        self.assertEquals(
            service2.icon,
            "http://p.ping.fm/static/icons/facebook.png")

    def test_get_triggers(self):
        response = Response(payload.sample_user_triggers_ok)
        trigger1, trigger2 = response.get_triggers()

        self.assertEquals(trigger1.id, "twt")
        self.assertEquals(trigger1.method, "microblog")
        self.assertEquals(trigger1.services[0].id, "twitter")
        self.assertEquals(trigger1.services[0].name, "Twitter")

        self.assertEquals(trigger2.id, "fb")
        self.assertEquals(trigger2.method, "status")
        self.assertEquals(trigger2.services[0].id, "facebook")
        self.assertEquals(trigger2.services[0].name, "Facebook")

    def test_get_latest_messages(self):
        response = Response(payload.sample_user_latest_ok)
        message1, message2, message3 = response.get_latest_messages()

        self.assertEquals(message1.id, "12345")
        self.assertEquals(message1.method, "blog")
        self.assertEquals(message1.rfc_time, "Tue, 15 Apr 2008 13:56:18 -0500")
        self.assertEquals(message1.unix_time, "1234567890")
        self.assertEquals(message1.title, "Just hangin' out!")
        self.assertEquals(message1.body, "Going to the store.")
        self.assertEquals(message1.location, None)
        self.assertEquals(message1.services[0].id, "blogger")
        self.assertEquals(message1.services[0].name, "Blogger")

        self.assertEquals(message2.id, "12346")
        self.assertEquals(message2.method, "microblog")
        self.assertEquals(message2.rfc_time, "Tue, 15 Apr 2008 13:56:18 -0500")
        self.assertEquals(message2.unix_time, "1234567890")
        self.assertEquals(message2.title, None)
        self.assertEquals(message2.body, "Going to the store.")
        self.assertEquals(message2.location, None)
        self.assertEquals(message2.services[0].id, "twitter")
        self.assertEquals(message2.services[0].name, "Twitter")

        self.assertEquals(message3.id, "12347")
        self.assertEquals(message3.method, "status")
        self.assertEquals(message3.rfc_time, "Tue, 15 Apr 2008 13:56:18 -0500")
        self.assertEquals(message3.unix_time, "1234567890")
        self.assertEquals(message3.title, None)
        self.assertEquals(message3.body, "is testing Ping.fm!")
        self.assertEquals(message3.location, "Tulsa, OK")
        self.assertEquals(message3.services[0].id, "twitter")
        self.assertEquals(message3.services[0].name, "Twitter")
        self.assertEquals(message3.services[1].id, "facebook")
        self.assertEquals(message3.services[1].name, "Facebook")
