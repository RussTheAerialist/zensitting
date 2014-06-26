import sseclient

BASE_URL = ""

def _null_callback(*args, **kwargs):
    # Do nothing since it's a null function
    pass

class EventWatcher(object):
    def __init__(self, device_id, authorization, start=_null_callback, end=_null_callback):
        self._device_id = device_id
        self._authorization = authorization
        self._url = "{0}/v1/devices/{1}/events".format(BASE_URL, self._device_id)
        self._start = start
        self._end = end

    def run(self):
        messages = sseclient.SSEClient(self._url, headers={
            'Authorization': "Bearer {0}".format(self._authorization)
        })
        for msg in messages:
            pass