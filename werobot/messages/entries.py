# -*- coding: utf-8 -*-
from werobot.utils import to_text


def __get_value(instance, path, default=None):
    dic = instance.__dict__
    for entry in path.split('.'):
        dic = dic.get(entry)
        if dic is None:
            return default
    return dic or default


class BaseEntry(object):
    def __init__(self, entry, default=None):
        self.entry = entry
        self.default = default


class IntEntry(BaseEntry):
    def __get__(self, instance, owner):
        try:
            v = int(__get_value(instance, self.entry, self.default))
        except TypeError:
            v = None
        return v


class FloatEntry(BaseEntry):
    def __get__(self, instance, owner):
        try:
            v = float(__get_value(instance, self.entry, self.default))
        except TypeError:
            v = None
        return v


class StringEntry(BaseEntry):
    def __get__(self, instance, owner):
        v = __get_value(instance, self.entry, self.default)
        if v is not None:
            return to_text(v)
        return v
