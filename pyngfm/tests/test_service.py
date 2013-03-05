from twisted.trial.unittest import TestCase

from pyngfm.service import SystemService, UserService


class ServiceTestCase(TestCase):

    def test_creation(self):
        service = SystemService(id="id1", name="name")
        self.assertEquals(service.id, "id1")
        self.assertEquals(service.name, "name")


class SystemServiceTestCase(TestCase):

    def test_creation(self):
        service = SystemService(id="id1", name="name", trigger="trigger",
                                url="http://url/", icon="http://icon.png")
        self.assertEquals(service.id, "id1")
        self.assertEquals(service.name, "name")
        self.assertEquals(service.trigger, "trigger")
        self.assertEquals(service.url, "http://url/")
        self.assertEquals(service.icon, "http://icon.png")

    def test_creation_with_exteded_call_syntax(self):
        kwds = dict(id="id1", name="name")
        service = UserService(trigger="trigger", url="http://url/",
                              icon="http://icon.png", **kwds)
        self.assertEquals(service.id, "id1")
        self.assertEquals(service.name, "name")
        self.assertEquals(service.trigger, "trigger")
        self.assertEquals(service.url, "http://url/")
        self.assertEquals(service.icon, "http://icon.png")

class UserServiceTestCase(TestCase):

    def test_creation(self):
        service = UserService(id="id1", name="name", trigger="trigger",
                                url="http://url/", icon="http://icon.png", 
                                methods=["method1", "method2"])
        self.assertEquals(service.id, "id1")
        self.assertEquals(service.name, "name")
        self.assertEquals(service.trigger, "trigger")
        self.assertEquals(service.url, "http://url/")
        self.assertEquals(service.icon, "http://icon.png")
        self.assertEquals(service.methods, ["method1", "method2"])

    def test_creation_with_exteded_call_syntax(self):
        kwds = dict(id="id1", name="name", trigger="trigger",
                    url="http://url/", icon="http://icon.png")
        service = UserService(methods=["method1", "method2"], **kwds)
        self.assertEquals(service.id, "id1")
        self.assertEquals(service.name, "name")
        self.assertEquals(service.trigger, "trigger")
        self.assertEquals(service.url, "http://url/")
        self.assertEquals(service.icon, "http://icon.png")
        self.assertEquals(service.methods, ["method1", "method2"])

    def test_creation_with_exteded_call_syntax_no_methods(self):
        kwds = dict(id="id1", name="name", trigger="trigger",
                    url="http://url/", icon="http://icon.png")
        service = UserService(**kwds)
        self.assertEquals(service.id, "id1")
        self.assertEquals(service.name, "name")
        self.assertEquals(service.trigger, "trigger")
        self.assertEquals(service.url, "http://url/")
        self.assertEquals(service.icon, "http://icon.png")
        self.assertEquals(service.methods, None)
