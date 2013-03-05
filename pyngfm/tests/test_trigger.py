from twisted.trial.unittest import TestCase

from pyngfm.service import Service
from pyngfm.trigger import Trigger


class TriggerTestCase(TestCase):

    def test_creation(self):
        services = [
            Service(id="id1", name="name1"),
            Service(id="id2", name="name2")]
        trigger = Trigger(id="id3", method="some.method", services=services)
        self.assertEquals(trigger.id, "id3")
        self.assertEquals(trigger.method, "some.method")
        self.assertEquals(trigger.services[0].id, "id1")
        self.assertEquals(trigger.services[0].name, "name1")
        self.assertEquals(trigger.services[1].id, "id2")
        self.assertEquals(trigger.services[1].name, "name2")
