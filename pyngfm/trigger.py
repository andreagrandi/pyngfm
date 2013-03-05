class Trigger(object):

    def __init__(self, id=None, method=None, services=None):
        self.id = id
        self.method = method
        self.services = services or []

    def set_id(self, id):
        self.id = id

    def set_method(self, method):
        self.method = method

    def add_service(self, service_id, service_name):
        service = {'id': service_id, 'name': service_name}
        self.services.append(service)
