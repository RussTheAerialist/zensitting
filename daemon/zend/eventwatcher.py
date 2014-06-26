def _null_callback(*args, **kwargs):
    # Do nothing since it's a null function
    pass

class EventWatcher(object):
    def __init__(self, device_id, start=_null_callback, end=_null_callback):
        self._device_id = device_id
        self._start = start
        self._end = end

        