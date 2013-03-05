from twisted.trial.unittest import TestCase

from pyngfm.client.base import BaseClient, BASE_URL
from pyngfm.exception import PingFMResponseError, PingFMValueError
from pyngfm.message import OK, FAIL
from pyngfm.testing import payload


class BaseClientTestCase(TestCase):


    def setUp(self):
        TestCase.setUp(self)
        self.client = BaseClient("key1", "key2")

    def test_client_creation(self):
        self.assertEquals(self.client.api_key, "key1")
        self.assertEquals(self.client.user_app_key, "key2")
        self.assertEquals(self.client.response, None)

    def test_set_api_key(self):
        self.client.set_api_key("newapikey")
        self.assertEquals(self.client.api_key, "newapikey")

    def test_set_user_app_key(self):
        self.client.set_user_app_key("newappkey")
        self.assertEquals(self.client.user_app_key, "newappkey")

    def test_set_common_parameters_simple(self):
        parameters = self.client._set_common_parameters()
        self.assertEquals(parameters, {"body": None})

    def test_set_common_parameters_all(self):
        passed_parameters = {
            "body": "the body",
            "title": "the title",
            "location": "the location",
            "media": "the media",
            "encoding": "the encoding",
            "exclude": "the exclude",
            "debug": True,
            "checksum": "the checksum",
            }
        parameters = self.client._set_common_parameters(**passed_parameters)
        self.assertEquals(parameters, {
            'body': 'the body',
            'checksum': 'the checksum',
            'debug': 1,
            'encoding': 'the encoding',
            'exclude': 'the exclude',
            'location': 'the location',
            'media': 'the media',
            'title': 'the title'})

    def test_build_url(self):
        unencoded_parameters = {
            "post_method": "GET",
            "spaces": "here there be spaces",
            "special_chars": "%&?",
            }
        url, parameters = self.client._build_url(
            "some_service", unencoded_parameters)
        expected_url = "%s%s" % (BASE_URL, "some_service")
        expected_parameters = ("post_method=GET&api_key=key1&"
                               "spaces=here+there+be+spaces&"
                               "special_chars=%25%26%3F&"
                               "user_app_key=key2")
        self.assertEquals(url, expected_url)
        self.assertEquals(parameters, expected_parameters)

    def test_build_url_with_multiple_services(self):
        unencoded_parameters = {
            "post_method": "GET",
            "services": ["facebook", "twitter", "identi.ca"]
            }
        url, parameters = self.client._build_url(
            "some_service", unencoded_parameters)
        expected_url = "%s%s" % (BASE_URL, "some_service")
        expected_parameters = ("services=facebook&"
                               "services=twitter&"
                               "services=identi.ca&"
                               "post_method=GET&api_key=key1&"
                               "user_app_key=key2")
        self.assertEquals(url, expected_url)
        self.assertEquals(parameters, expected_parameters)

    def test_handle_response_ok(self):
        response = self.client._handle_response(payload.sample_response_ok)
        self.assertEquals(response.status, OK)

    def test_handle_response_fail(self):
        self.assertRaises(
            PingFMResponseError,
            self.client._handle_response,
            payload.sample_response_fail)
        try:
            self.client._handle_response(payload.sample_response_fail)
        except PingFMResponseError:
            self.assertEquals(self.client.response.status, FAIL)


class CommonClientTestCase(TestCase):
    """Unit tests that are common to both the async and sync clients."""

    def setUp(self):
        TestCase.setUp(self)
        self.client = None

    def test_user_post_no_body(self):
        if not self.client:
            return
        self.assertRaises(PingFMValueError, self.client.user_post, "microblog")
        try:
            self.client.user_post("microblog")
        except PingFMValueError, error:
            self.assertEquals(
                error.message,
                "The 'body' parameter must have a value.")

    def test_user_post_bad_post_method(self):
        if not self.client:
            return
        self.assertRaises(PingFMValueError, self.client.user_post, "microhack")
        try:
            self.client.user_post("microhack")
        except PingFMValueError, error:
            self.assertEquals(
                error.message,
                "The 'post_method' must be one of blog, microblog, status.")

    def test_user_tpost_no_body(self):
        if not self.client:
            return
        self.assertRaises(
            PingFMValueError, self.client.user_tpost, "my_trigger")
        try:
            self.client.user_tpost("my_trigger")
        except PingFMValueError, error:
            self.assertEquals(
                error.message,
                "The 'body' parameter must have a value.")
