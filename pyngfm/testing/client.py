from StringIO import StringIO

from twisted.internet.defer import succeed


class FakeOpener(object):

    def __init__(self, return_data):
        self.return_data = return_data
        self.url = None


class FakeGetPage(FakeOpener):
    """
    A fake page object with a getPage function for use in unit tests that use
    the Twisted getPage web client function.
    """
    def getPage(self, url, method="", postdata=None, headers=None):
        self.url = url
        self.method = method
        self.postdata = postdata
        self.headers = headers
        return succeed(self.return_data)


class FakeURLOpen(FakeOpener):
    """
    A fake URL open object with a urlopen function for use in unit tests that
    use the urllb2.urlopen.
    """
    def urlopen(self, url, data=None):
        self.url = url
        self.data = data
        return StringIO(self.return_data)

