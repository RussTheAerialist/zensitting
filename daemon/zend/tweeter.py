import tweepy

cc_msg = "// @RussellHay"

class Tweeter(object):
    def __init__(self, consumer_token, consumer_secret, access_key, access_secret, device_id, device_token, gen_method):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_key, access_secret)

        self._api = tweepy.API(auth)
        self._generator = gen_method
        self._spark = (device_id, device_token)

    def produce(self, msg=None, cc=False):
        if msg is None:
            msg = self._generator()

        if cc is not None and len(msg) < 140 - len(cc_msg) - 1:
            msg = "{0} {1}".format(msg, cc_msg)
        self._api.update_status(msg)

    def __call__(self):
        # TODO: setup the daemon polling for events
        pass