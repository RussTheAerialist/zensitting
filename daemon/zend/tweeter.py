import datetime

import tweepy

import zend.eventwatcher

cc_msg = "// @RussellHay"

class Tweeter(object):
    def __init__(self, consumer_token, consumer_secret, access_key, access_secret, device_id, device_token, gen_method):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_key, access_secret)

        self._api = tweepy.API(auth)
        self._generator = gen_method
        self._spark = (device_id, device_token)
        self._started_at = None

    def produce(self, msg=None, cc=False):
        if msg is None:
            msg = self._generator()

        if cc and len(msg) < 140 - len(cc_msg) - 1:
            msg = "{0} {1}".format(msg, cc_msg)
        self._api.update_status(msg)

    def start_sitting(self, id, data):
        print("Butt Detected")
        if self._started_at is not None:
            print("Received Start without a previous end!")
            self.produce("Something Strange is happenign with the Meditation Bench.")

        self._started_at = datetime.datetime.now()
        self.produce()

    @staticmethod
    def calculate_elapsed_time(delta):
        total_seconds = delta.total_seconds()
        seconds = int(total_seconds % 60)
        minutes = int(total_seconds / 60)
        hours = int(minutes / 60)
        minutes = minutes % 60
        elapsed_time = "{0}h {1}m {2}s".format(hours, minutes, seconds)
        return elapsed_time

    def end_sitting(self, id, data):
        if self._started_at is None:
            print("Received End without a Start!")
            self.produce("Something Weird is happening with the Meditation Bench.")
            return

        now = datetime.datetime.now()
        delta = now - self._started_at
        elapsed_time = self.calculate_elapsed_time(delta)
        print("Sat for {0}".format(elapsed_time))

        self.produce("Bench in use for {0}".format(elapsed_time), cc=True)
        self._started_at = None


    def __call__(self):
        watcher = zend.eventwatcher.EventWatcher(*self._spark, start=self.start_sitting, end=self.end_sitting)
        watcher.run()

if __name__ == "__main__":
    data = [
        datetime.timedelta(seconds=1),
        datetime.timedelta(minutes=1, seconds=1),
        datetime.timedelta(hours=1, seconds=1, minutes=1),
        datetime.timedelta(minutes=90, seconds=61),
        datetime.timedelta()
    ]
    for datum in data:
        print(datum, Tweeter.calculate_elapsed_time(datum))
