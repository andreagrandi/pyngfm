import urllib

from pyngfm.exception import PingFMValueError, PingFMResponseError
from pyngfm.message import Response, FAIL
from pyngfm.util import get_boolean_as_int


BASE_URL = "http://api.ping.fm/v1/"
VALID_POST_METHODS = ["blog", "microblog", "status"]


class BaseClient(object):

    def __init__(self, api_key, user_app_key):
        # Note that both of these keys are necessary to use the library.
        # User's application key; you can get your key here:
        #   http://ping.fm/key/
        self.user_app_key = user_app_key
        # The developer's API key; if you want to use the PyngFM library,
        # create a developer API key here:
        #   http://ping.fm/developers/
        # Eventually, we may include a reviewed/approved PyngFM API key.
        self.api_key = api_key
        self.response = None

    def _build_url(self, service, parameters):
        """
        Given a Ping.fm service and a parameters dict, provide the URL for the
        remote call to ping.fm as well as the data that will be sent with the
        request.
        """
        url = BASE_URL + str(service)
        if self.user_app_key:
            parameters['user_app_key'] = self.user_app_key
        if self.api_key:
            parameters['api_key'] = self.api_key
        data = urllib.urlencode(parameters, doseq=True)
        return (url, data)

    def _handle_response(self, response):
        self.response = Response(response)
        if self.response.status == FAIL:
            raise PingFMResponseError(self.response.get_message())
        return self.response

    def _remote_call(self, service, parameters={}):
        """Call a method on the ping.fm server."""
        raise NotImplementedError

    def _set_common_parameters(self, **kwds):
        parameters = {}
        parameters['body'] = kwds.get('body')
        title = kwds.get('title')
        if title:
            parameters['title'] = title
        location = kwds.get('location')
        if location:
            parameters['location'] = location
        media = kwds.get('media')
        if media:
            parameters['media'] = media
        encoding = kwds.get('encoding')
        if encoding:
            parameters['encoding'] = encoding
        exclude = kwds.get('exclude')
        if exclude:
            parameters['exclude'] = exclude
        debug = kwds.get('debug')
        if debug is not None:
            parameters["debug"] = get_boolean_as_int(debug)
        checksum = kwds.get('checksum')
        if checksum:
            parameters['checksum'] = checksum
        return parameters

    def _do_post_method_check(self, post_method):
        if post_method not in VALID_POST_METHODS:
            valid = ", ".join(VALID_POST_METHODS)
            raise PingFMValueError("The 'post_method' must be one of %s." % (
                valid,))

    def _do_body_check(self, body):
        if not body:
            raise PingFMValueError("The 'body' parameter must have a value.")

    def set_api_key(self, key):
        """
        Sets the API key, if not already set.  It can also be used to change
        the key.
        """
        self.api_key = key

    def set_user_app_key(self, key):
        """
        Sets the User's application key, if not already set.  It can also be
        used to change the key.
        """
        self.user_app_key = key
