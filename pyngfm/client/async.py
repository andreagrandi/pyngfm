from twisted.web.client import getPage

from pyngfm.client.base import BaseClient
from pyngfm.message import OK


class PingFMAsyncClient(BaseClient):

    def _remote_call(self, service, parameters={}, callback=None):
        url, data = self._build_url(service, parameters)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        d = getPage(url, method="POST", postdata=data, headers=headers)
        d.addCallback(self._handle_response)
        d.addErrback(self._handle_error)
        if callback:
            d.addCallback(callback)
        return d

    def _get_response_status(self, response):
        return response.status

    def _handle_error(self, error):
        print error

    def _get_services(self, response):
        if response.status == OK:
            return response.get_services()

    def user_validate(self):
        def assert_status(response):
            return response.status == OK
        return self._remote_call("user.validate", callback=assert_status)

    def user_post(self, post_method, **kwds):
        """
        Public API function: user.post: posts a message to the user's Ping.fm
        services.

        @param post_method
          Posting method.  Either "blog", "microblog" or "status."
        @param body
          Message body.
        @param title
          Title of the posted message.  This will only appear if the specified
          service supports a title field.  Otherwise, it will be discarded.
        @param service
            A single service to post to. If the posted method is not supported
            by service, the request will return an error.
        @param tags
            A single tag or a list of tags to include with the post.
        @param mood
        @param location
        @param media
        @param encoding
        @param exclude
        @param debug
        @param checksum
        """
        self._do_post_method_check(post_method)
        self._do_body_check(kwds.get("body"))
        parameters = self._set_common_parameters(**kwds)
        parameters["post_method"] = post_method
        service = kwds.get("service")
        if service:
            parameters['service'] = service
        tags = kwds.get("tags")
        if tags:
            parameters["tags"] = tags
        mood = kwds.get("mood")
        if mood:
            parameters['mood'] = mood
        return self._remote_call("user.post", parameters,
                                 callback=self._get_response_status)

    def user_tpost(self, trigger, **kwds):
        """
        Public API function: user.tpost: posts a message to the user's Ping.fm
        services using one of their custom triggers.

        @param trigger
          Custom trigger the user has defined from the Ping.fm website.
        @param body
          Message body.
        @param title
          Title of the posted message.  This will only appear if the specified
          service supports a title field.  Otherwise, it will be discarded.
        @param location
        @param media
        @param encoding
        @param exclude
        @param debug
        @param checksum
        """
        self._do_body_check(kwds.get("body"))
        parameters = self._set_common_parameters(**kwds)
        parameters['trigger'] = trigger
        return self._remote_call("user.tpost", parameters,
                                 callback=self._get_response_status)

    def system_services(self):
        """
        Public API function: system.services: Return a complete list of
        supported services.

        @return
          A list of SystemService objects containing all informations about
          Ping.fm supported services
        """
        return self._remote_call("system.services",
                                 callback=self._get_services)

    def user_key(self, mobile_key):
        """
        Public API function: user.key: Will exchange a mobile application key
        for a functional application key.  This is for mobile apps that would
        offer an easier way of authenticating users.

        @param mobile_key: Mobile application key. (Users can be prompted to
            get their key here: http://ping.fm/key/).
        @return
          A User Application's key
        """

        def get_key(response):
            if response.status == OK:
                return response.get_key()

        parameters = {}
        parameters['mobile_key'] = mobile_key
        return self._remote_call("user.key", parameters, callback=get_key)

    def user_services(self):
        """
        Public API function: system.services: Return a complete list of
        supported services.

        @return
          A list of SystemService objects containing all informations about
          Ping.fm supported services
        """
        return self._remote_call("user.services", callback=self._get_services)

    def user_triggers(self):
        """
        Public API function: user.triggers: Returns a user's custom triggers.

        @return
          A list of Trigger objects containing all informations about
          user's custom triggers.
        """

        def get_triggers(response):
            if response.status == OK:
                return response.get_triggers()

        return self._remote_call("user.triggers", callback=get_triggers)

    def user_latest(self, limit=25, order="DESC"):
        """
        Public API function: user.latest: Returns the last 25 messages a
        user has posted through Ping.fm.

        @param limit: Limit the results returned.  Default is 25.
        @param order: Which direction to order the returned results by date.
            Default is DESC (Descending).
        @return: A list of Message object containing the last messages a user
            has posted trough Ping.fm.
        """

        def get_latest_messages(response):
            if response.status == OK:
                return response.get_latest_messages()

        parameters = {
            "limit": limit,
            "order": order}
        return self._remote_call("user.latest", parameters,
                                 callback=get_latest_messages)
