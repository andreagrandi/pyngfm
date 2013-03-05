from urllib2 import urlopen

from pyngfm.client.base import BaseClient
from pyngfm.message import OK


class PingFMSyncClient(BaseClient):

    def _remote_call(self, service, parameters={}):
        """
        Call a method on the ping.fm server.

        @param service
          The end of the URL to fetch.  For example user.services will
          become http://api.ping.fm/v1/user.services when requesting from the
          server.
        @param parameters
          The parameters to pass in over POST.  The user's app key and the API
          key are automatically added.
        @return TODO: document me!
        """
        response = urlopen(*self._build_url(service, parameters)).read()
        return self._handle_response(response)

    def user_validate(self):
        """
        Public API function: user.validate: validates the
        given user's app key.

        @return
          A boolean of whether the app key is correct.
        """
        response = self._remote_call("user.validate")
        return response.status == OK

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
            parameters["service"] = service
        tags = kwds.get("tags")
        if tags:
            parameters["tags"] = tags
        mood = kwds.get("mood")
        if mood:
            parameters['mood'] = mood
        response = self._remote_call("user.post", parameters)
        return response.status

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
        parameters["trigger"] = trigger
        response = self._remote_call("user.tpost", parameters)
        return response.status

    def system_services(self):
        """
        Public API function: system.services: Return a complete list of
        supported services.

        @return
          A list of SystemService objects containing all informations about
          Ping.fm supported services
        """
        response = self._remote_call("system.services")
        if response.status == OK:
            return response.get_services()

    def user_key(self, mobile_key):
        """
        Public API function: user.key: Will exchange a mobile application key
        for a functional application key.  This is for mobile apps that would
        offer an easier way of authenticating users.

        @return
          A User Application's key
        """
        parameters = {}
        parameters["mobile_key"] = mobile_key
        response = self._remote_call("user.key", parameters)
        if response.status == OK:
            return response.get_key()

    def user_services(self):
        """
        Public API function: user.services: Returns a list of services the
        particular user has set up through Ping.fm.

        @return
          A list of UserService objects containing all informations about
          services the particular user has set up through Ping.fm.
        """
        response = self._remote_call("user.services")
        if response.status == OK:
            return response.get_services()

    def user_triggers(self):
        """
        Public API function: user.triggers: Returns a user's custom triggers.

        @return
          A list of Trigger objects containing all informations about
          user's custom triggers.
        """
        response = self._remote_call("user.triggers")
        if response.status == OK:
            return response.get_triggers()

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
        parameters = {
            "limit": limit,
            "order": order}
        response = self._remote_call("user.latest", parameters)
        if response.status == OK:
            return response.get_latest_messages()


PingFMClient = PingFMSyncClient
