#!/usr/bin/python
import sys
from ConfigParser import SafeConfigParser

from twisted.internet import reactor

from pyngfm.client import PingFMAsyncClient


def checkMessage(message):
    """
    If the message is too long, we need to abort and give the user a change to
    ammend it.
    """
    if len(message) > 140:
        print "Message is too long! (%s chars)" % len(message)
        sys.exit(1)


def getKeys():
    """
    Reads the sensitive key information from a config file that only your user
    has permissions to read.

    Note that this code is blocking, because it's readying from the file
    system. If we really wanted to make sure that no code in this script
    blocked, we'd execute this function in a thread with Twisted'd
    deferToThread function.
    """
    cred_file = "/etc/ping.fm.creds"
    config = SafeConfigParser()
    config.read([cred_file])
    api_key = config.get("default", "api-key")
    user_app_key = config.get("default", "user-app-key")
    return api_key, user_app_key


def pingIt(message):
    """
    Send a message to the server.
    """
    def check_result(status):
        print "Status:", status

    def check_error(error):
        print "Status:", error.getErrorMessage()

    def finish(ignored):
        reactor.stop()

    pinger = PingFMAsyncClient(*getKeys())
    deferred = pinger.user_post("status", body=message)
    deferred.addErrback(check_error)
    deferred.addCallback(check_result)
    deferred.addCallback(finish)


if __name__ == "__main__":
    message = " ".join(sys.argv[1:])
    checkMessage(message)
    pingIt(message)
    reactor.run()
