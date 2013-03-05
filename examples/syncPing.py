#!/usr/bin/python
import sys
from ConfigParser import SafeConfigParser

from pyngfm.client import PingFMSyncClient
from pyngfm.message import FAIL


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
    pinger = PingFMSyncClient(*getKeys())
    try:
        pinger.user_post("status", body=message)
        print "Status:", pinger.response.status
    except Exception, error:
        if pinger.response.status == FAIL:
            print "Status:", pinger.response.status
        print e


if __name__ == "__main__":
    message = " ".join(sys.argv[1:])
    checkMessage(message)
    pingIt(message)
