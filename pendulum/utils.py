# -*- coding: utf-8 -*-


class CallableTimestamp(int):
    """
    An int object representing a timestamp that
    returns a float when called.

    Its purpose is backward compatibility from the
    ``timestamp`` property that should be a method.
    """

    def __init__(self, value, float_=None):
        self._float = float_ or value

        super(CallableTimestamp, self).__init__()

    def set_float(self, float_):
        self._float = float_

    def __call__(self, as_int=False):
        if as_int:
            return self

        return self._float