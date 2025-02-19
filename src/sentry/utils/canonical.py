from __future__ import annotations

import copy
from collections.abc import Mapping, MutableMapping
from typing import TypeVar

import sentry_sdk
from django.conf import settings

K = TypeVar("K")
V = TypeVar("V")

__all__ = ("CanonicalKeyDict", "CanonicalKeyView", "get_canonical_name")


LEGACY_KEY_MAPPING = {
    "exception": ("sentry.interfaces.Exception",),
    "logentry": ("sentry.interfaces.Message", "message"),
    "stacktrace": ("sentry.interfaces.Stacktrace",),
    "template": ("sentry.interfaces.Template",),
    "request": ("sentry.interfaces.Http",),
    "user": ("sentry.interfaces.User",),
    "csp": ("sentry.interfaces.Csp",),
    "nel": ("sentry.interfaces.Nel",),
    "breadcrumbs": ("sentry.interfaces.Breadcrumbs",),
    "contexts": ("sentry.interfaces.Contexts",),
    "threads": ("sentry.interfaces.Threads",),
    "debug_meta": ("sentry.interfaces.DebugMeta",),
}


CANONICAL_KEY_MAPPING = {
    "message": ("logentry", "sentry.interfaces.Message"),
    "sentry.interfaces.Exception": ("exception",),
    "sentry.interfaces.Message": ("logentry",),
    "sentry.interfaces.Stacktrace": ("stacktrace",),
    "sentry.interfaces.Template": ("template",),
    "sentry.interfaces.Http": ("request",),
    "sentry.interfaces.User": ("user",),
    "sentry.interfaces.Csp": ("csp",),
    "sentry.interfaces.Nel": ("nel",),
    "sentry.interfaces.Breadcrumbs": ("breadcrumbs",),
    "sentry.interfaces.Contexts": ("contexts",),
    "sentry.interfaces.Threads": ("threads",),
    "sentry.interfaces.DebugMeta": ("debug_meta",),
}


def get_canonical_name(key):
    return CANONICAL_KEY_MAPPING.get(key, (key,))[0]


def get_legacy_name(key):
    return LEGACY_KEY_MAPPING.get(key, (key,))[0]


class CanonicalKeyView(Mapping):
    def __init__(self, data):
        self.data = data
        self._len = len({get_canonical_name(key) for key in self.data})

    def copy(self):
        return self

    __copy__ = copy

    def __len__(self):
        return self._len

    def __iter__(self):
        # Preserve the order of iteration while prioritizing canonical keys
        keys = list(self.data)
        for key in keys:
            canonicals = CANONICAL_KEY_MAPPING.get(key, ())
            if not canonicals:
                yield key
            elif all(k not in keys for k in canonicals):
                yield canonicals[0]

    def __getitem__(self, key):
        canonical = get_canonical_name(key)
        for k in (canonical,) + LEGACY_KEY_MAPPING.get(canonical, ()):
            if k in self.data:
                return self.data[k]

        raise KeyError(key)

    def __repr__(self):
        return self.data.__repr__()


class CanonicalKeyDict(MutableMapping[K, V]):
    def __init__(self, data: Mapping[K, V], legacy: bool | None = None) -> None:
        self.legacy = legacy
        self.__init(data)

    @sentry_sdk.tracing.trace
    def __init(self, data: Mapping[K, V]) -> None:
        legacy = self.legacy
        if legacy is None:
            legacy = settings.PREFER_CANONICAL_LEGACY_KEYS
        norm_func = get_legacy_name if legacy else get_canonical_name
        self._norm_func = norm_func
        self.data: dict[K, V] = {}
        for key, value in data.items():
            canonical_key = norm_func(key)
            if key == canonical_key or canonical_key not in self.data:
                self.data[canonical_key] = value

    def __getstate__(self):
        state = dict(self.__dict__)
        state.pop("_norm_func", None)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__init(state["data"])

    def copy(self):
        rv = object.__new__(self.__class__)
        rv._norm_func = self._norm_func
        rv.data = copy.copy(self.data)
        return rv

    __copy__ = copy

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, key):
        return self._norm_func(key) in self.data

    def __getitem__(self, key):
        return self.data[self._norm_func(key)]

    def __setitem__(self, key, value):
        self.data[self._norm_func(key)] = value

    def __delitem__(self, key):
        del self.data[self._norm_func(key)]

    def __repr__(self):
        return f"CanonicalKeyDict({self.data.__repr__()})"


CANONICAL_TYPES = (CanonicalKeyDict, CanonicalKeyView)
