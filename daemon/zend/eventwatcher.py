import sseclient

import requests.exceptions

BASE_URL = "https://api.spark.io"

def _null_callback(*args, **kwargs):
    # Do nothing since it's a null function
    pass

class EventWatcher(object):
    def __init__(self, device_id, authorization, start=_null_callback, end=_null_callback):
        self._device_id = device_id
        self._authorization = authorization
        self._url = "{0}/v1/devices/{1}/events".format(BASE_URL, self._device_id)
        self._map = {
            u'start-detect': start,
            u'end-detect': end
        }

    def run(self):
        print "curl -H \"Authorization: Bearer {0}\" {1}".format(self._authorization, self._url)

        try:
            messages = sseclient.SSEClient(self._url, headers={
                'Authorization': "Bearer {0}".format(self._authorization)
            })
            for msg in messages:
                if msg.event in self._map:
                    self._map[msg.event](msg.event, msg.data)
                else:
                    print("Unknown Event Type, Ignoring: {0}".format(msg.id))
                    print(msg.id, msg.event)

        except requests.exceptions.HTTPError, ex:
            print(ex.response.text)
            raise