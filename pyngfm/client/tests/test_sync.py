from pyngfm.client import sync
from pyngfm.client.tests.test_base import CommonClientTestCase
from pyngfm.message import OK
from pyngfm.testing  import payload
from pyngfm.testing.client  import FakeURLOpen


class SyncClientTestCase(CommonClientTestCase):

    def setUp(self):
        CommonClientTestCase.setUp(self)
        self.client = sync.PingFMSyncClient("key1", "key2")

    def test_remote_call_no_parameters(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_response_ok)
        sync.urlopen = getter.urlopen
        self.client._remote_call("test.service")
        self.assertEquals(self.client.response.status, OK)
        sync.urlopen = original_urlopen

    def test_remote_call_with_parameters(self):
        data = {"something": 1,
                "something-else": 2}
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_response_ok)
        sync.urlopen = getter.urlopen
        self.client._remote_call("test.service", parameters=data)
        self.assertEquals(self.client.response.status, OK)
        sync.urlopen = original_urlopen

    def test_user_validate(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_user_app_key_ok)
        sync.urlopen = getter.urlopen
        success = self.client.user_validate()
        self.assertEquals(self.client.response.status, OK)
        self.assertTrue(success)
        sync.urlopen = original_urlopen

    def test_system_services(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_system_services_ok)
        sync.urlopen = getter.urlopen
        services = self.client.system_services()
        self.assertEquals(self.client.response.status, OK)
        self.assertEquals(len(services), 2)
        self.assertEquals(services[0].id, "bebo")
        self.assertEquals(services[1].id, "blogger")
        sync.urlopen = original_urlopen

    def test_user_post(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_user_post_ok)
        sync.urlopen = getter.urlopen
        status = self.client.user_post("blog", body="great blog post")
        self.assertEquals(status, OK)
        self.assertTrue("body=great+blog+post" in getter.data)
        sync.urlopen = original_urlopen

    def test_user_post_all_parameters(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_user_post_ok)
        sync.urlopen = getter.urlopen
        status = self.client.user_post(
            "status", body="test status message", title="title",
            service="facebook", tags=["happy", "funball"], location="here",
            media="somemedia", encoding="utf-8", exclude="athing", debug=False,
            checksum="cksumstuff", mood="stoked")
        self.assertEquals(status, OK)
        self.assertTrue("user.post" in getter.url)
        self.assertTrue("body=test+status+message" in getter.data)
        self.assertTrue("encoding=utf-8" in getter.data)
        self.assertTrue("media=somemedia" in getter.data)
        self.assertTrue("title=title" in getter.data)
        self.assertTrue("service=facebook" in getter.data)
        self.assertTrue("tags=happy" in getter.data)
        self.assertTrue("tags=funball" in getter.data)
        self.assertTrue("mood=stoked" in getter.data)
        self.assertTrue("location=here" in getter.data)
        self.assertTrue("checksum=cksumstuff" in getter.data)
        self.assertTrue("debug=0" in getter.data)
        self.assertTrue("exclude=athing" in getter.data)
        self.assertTrue("api_key=key1" in getter.data)
        sync.urlopen = original_urlopen

    def test_user_key(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_user_key_ok)
        sync.urlopen = getter.urlopen
        key = self.client.user_key("mobile_key")
        self.assertEquals(self.client.response.status, OK)
        self.assertEquals(key, "abcdeasdadsdghasdfaslkdjfa012345-1234567890")
        sync.urlopen = original_urlopen

    def test_user_services(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_user_services_ok)
        sync.urlopen = getter.urlopen
        services = self.client.user_services()
        self.assertEquals(self.client.response.status, OK)
        self.assertEquals(len(services), 2)
        self.assertEquals(services[0].id, "twitter")
        self.assertEquals(services[1].id, "facebook")
        sync.urlopen = original_urlopen

    def test_user_triggers(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_user_triggers_ok)
        sync.urlopen = getter.urlopen
        triggers = self.client.user_triggers()
        self.assertEquals(self.client.response.status, OK)
        self.assertEquals(triggers[0].id, "twt")
        self.assertEquals(triggers[1].id, "fb")
        sync.urlopen = original_urlopen

    def test_user_latest(self):
        original_urlopen = sync.urlopen
        getter = FakeURLOpen(payload.sample_user_latest_ok)
        sync.urlopen = getter.urlopen
        messages = self.client.user_latest()
        self.assertEquals(self.client.response.status, OK)
        self.assertEquals(messages[0].id, "12345")
        self.assertEquals(messages[1].id, "12346")
        self.assertEquals(messages[2].id, "12347")
        sync.urlopen = original_urlopen
