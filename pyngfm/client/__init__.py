from pyngfm.client.sync import PingFMClient, PingFMSyncClient
try:
    from pyngfm.client.async import PingFMAsyncClient
except ImportError:
    # Looks like Twisted might not be installed
    pass
