class Service(object):

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name


class SystemService(Service):

    def __init__(self, trigger=None, url=None, icon=None, **kwds):
        super(SystemService, self).__init__(**kwds)
        self.trigger = trigger
        self.url = url
        self.icon = icon

    def set_trigger(self, trigger):
        self.trigger = trigger

    def set_url(self, url):
        self.url = url

    def set_icon(self, icon):
        self.icon = icon


class UserService(SystemService):

    def __init__(self, methods=None, **kwds):
        super(UserService, self).__init__(**kwds)
        self.methods = methods

    def set_methods(self, methods):
        self.methods = methods
