from pyngfm.client import async
from pyngfm.client.tests.test_base import CommonClientTestCase
from pyngfm.message import Message, Response, OK
from pyngfm.service import SystemService, UserService
from pyngfm.testing import payload
from pyngfm.testing.client import FakeGetPage
from pyngfm.trigger import Trigger


class AsyncClientTestCase(CommonClientTestCase):

    def setUp(self):
        CommonClientTestCase.setUp(self)
        self.client = async.PingFMAsyncClient("key1", "key2")

    def cleanup(self, ignored, module, attr, original):
        setattr(module, attr, original)

    def test_remote_call(self):

        def check_result(response, getter):
            self.assertEquals(response.status, OK)
            self.assertEquals(response.transaction, "12345")
            self.assertEquals(response.method, "user.services")
            expected_url = ("http://api.ping.fm/v1/user.services")
            self.assertEquals(getter.url, expected_url)
            self.assertTrue("user_app_key=key2&api_key=key1" in
                            getter.postdata)

        getter = FakeGetPage(payload.sample_response_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client._remote_call("user.services")
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_get_response_status(self):
        response = Response(payload.sample_response_ok)
        self.assertEquals(response.status, OK)

    def test_user_validate(self):

        def check_result(result, getter):
            self.assertEquals(result, True)
            self.assertTrue("user.validate" in getter.url)

        getter = FakeGetPage(payload.sample_user_app_key_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_validate()
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_user_post(self):

        def check_result(result, getter):
            self.assertEquals(result, OK)
            self.assertTrue("user.post" in getter.url)
            self.assertTrue("body=test+status+message" in getter.postdata)

        getter = FakeGetPage(payload.sample_user_post_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_post("status", body="test status message")
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_user_post_all_parameters(self):

        def check_result(result, getter):
            self.assertEquals(result, OK)
            self.assertTrue("user.post" in getter.url)
            self.assertTrue("body=test+status+message" in getter.postdata)
            self.assertTrue("encoding=utf-8" in getter.postdata)
            self.assertTrue("media=somemedia" in getter.postdata)
            self.assertTrue("title=title" in getter.postdata)
            self.assertTrue("service=facebook" in getter.postdata)
            self.assertTrue("tags=happy" in getter.postdata)
            self.assertTrue("tags=funball" in getter.postdata)
            self.assertTrue("mood=stoked" in getter.postdata)
            self.assertTrue("location=here" in getter.postdata)
            self.assertTrue("checksum=cksumstuff" in getter.postdata)
            self.assertTrue("debug=0" in getter.postdata)
            self.assertTrue("exclude=athing" in getter.postdata)
            self.assertTrue("api_key=key1" in getter.postdata)

        getter = FakeGetPage(payload.sample_user_post_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_post(
            "status", body="test status message", title="title",
            service="facebook", tags=["happy", "funball"], location="here",
            media="somemedia", encoding="utf-8", exclude="athing", debug=False,
            checksum="cksumstuff", mood="stoked")
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_user_tpost_all_parameters(self):

        def check_result(result, getter):
            self.assertEquals(result, OK)
            self.assertTrue("user.tpost" in getter.url)
            self.assertTrue("body=test+status+message" in getter.postdata)
            self.assertTrue("encoding=utf-8" in getter.postdata)
            self.assertTrue("media=somemedia" in getter.postdata)
            self.assertTrue("title=title" in getter.postdata)
            self.assertTrue("location=here" in getter.postdata)
            self.assertTrue("checksum=cksumstuff" in getter.postdata)
            self.assertTrue("debug=0" in getter.postdata)
            self.assertTrue("exclude=athing" in getter.postdata)
            self.assertTrue("api_key=key1" in getter.postdata)
            self.assertTrue("trigger=my_trigger" in getter.postdata)

        getter = FakeGetPage(payload.sample_user_post_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_tpost(
            "my_trigger",
            post_method="status", body="test status message", title="title",
            services=["facebook", "twitter"], location="here",
            media="somemedia", encoding="utf-8", exclude="athing", debug=False,
            checksum="cksumstuff")
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_system_services(self):

        def check_result(services, getter):
            self.assertTrue("system.services" in getter.url)
            self.assertEquals(len(services), 2)
            self.assertTrue(isinstance(services[0], SystemService))
            self.assertEquals(services[0].id, "bebo")
            self.assertEquals(services[1].id, "blogger")

        getter = FakeGetPage(payload.sample_system_services_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.system_services()
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_user_key(self):

        def check_result(key, getter):
            self.assertTrue("user.key" in getter.url)
            self.assertTrue("mobile_key=mymobilekey" in getter.postdata)
            self.assertEquals(
                key, "abcdeasdadsdghasdfaslkdjfa012345-1234567890")

        getter = FakeGetPage(payload.sample_user_key_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_key("mymobilekey")
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_user_services(self):

        def check_result(services, getter):
            self.assertTrue("user.services" in getter.url)
            self.assertEquals(len(services), 2)
            self.assertTrue(isinstance(services[0], UserService))
            self.assertEquals(services[0].id, "twitter")
            self.assertEquals(services[1].id, "facebook")

        getter = FakeGetPage(payload.sample_user_services_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_services()
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_user_triggers(self):

        def check_result(triggers, getter):
            self.assertTrue("user.triggers" in getter.url)
            self.assertEquals(len(triggers), 2)
            self.assertTrue(isinstance(triggers[0], Trigger))
            self.assertEquals(triggers[0].id, "twt")
            self.assertEquals(len(triggers[0].services), 1)
            self.assertEquals(triggers[1].id, "fb")
            self.assertEquals(len(triggers[1].services), 1)

        getter = FakeGetPage(payload.sample_user_triggers_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_triggers()
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred

    def test_user_latest(self):

        def check_result(messages, getter):
            self.assertTrue("user.latest" in getter.url)
            self.assertEquals(len(messages), 3)
            self.assertTrue(isinstance(messages[0], Message))
            self.assertEquals(messages[0].id, "12345")
            self.assertEquals(len(messages[0].services), 1)
            self.assertEquals(messages[1].id, "12346")
            self.assertEquals(len(messages[1].services), 1)
            self.assertEquals(messages[1].id, "12346")
            self.assertEquals(len(messages[1].services), 1)

        getter = FakeGetPage(payload.sample_user_latest_ok)
        original_getPage = async.getPage
        async.getPage = getter.getPage

        deferred = self.client.user_latest()
        deferred.addCallback(check_result, getter)
        deferred.addCallback(self.cleanup, async, "getPage", original_getPage)
        return deferred
