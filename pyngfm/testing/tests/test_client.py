from twisted.trial.unittest import TestCase

from pyngfm.testing.client import FakeGetPage


class FakeGetPageTestCase(TestCase):

    def test_getPage(self):

        def check_result(result, getter):
            self.assertEquals(result, "<html><body>Hey there!</body></html>")
            self.assertEquals(getter.url, "http://test.com/some/url/")

        getter = FakeGetPage("<html><body>Hey there!</body></html>")
        deferred = getter.getPage("http://test.com/some/url/")
        deferred.addCallback(check_result, getter)
