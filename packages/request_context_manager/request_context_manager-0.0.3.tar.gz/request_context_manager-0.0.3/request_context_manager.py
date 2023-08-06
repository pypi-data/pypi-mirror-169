from contextlib import contextmanager
from threading import local
from typing import Any


UNDEFINED = object()


class Errors:
    class AlreadyUnderContext(Exception):
        pass

    class OutsideContext(Exception):
        pass

    class AttrNotFound(Exception):
        pass


class RequestContext:
    def __init__(self, name):
        self.name = name
        self.data = dict()


class RequestContextManager:
    def __init__(self, name, allow_nested=False):
        self._tls = local()
        self._name = name
        self._allow_nested = allow_nested

    @property
    def _context_stack(self):
        if not hasattr(self._tls, 'context_stack'):
            self._tls.context_stack = []
        return self._tls.context_stack

    def _push_request_context(self):
        self._context_stack.append(RequestContext(self._name))

    def _pop_request_context(self):
        self._context_stack.pop()

    def _get_current_request_context(self) -> RequestContext:
        return self._context_stack[-1] if self._context_stack else None

    def is_under_request_context(self):
        return True if self._context_stack else False

    @contextmanager
    def under_request_context(self):
        if self.is_under_request_context() and not self._allow_nested:
            current_request_context = self._get_current_request_context()
            raise Errors.AlreadyUnderContext(f'You are already under "{current_request_context.name}" context')

        self._push_request_context()
        try:
            yield
        finally:
            self._pop_request_context()

    def set_attr(self, attr: str, value: Any):
        if not self.is_under_request_context():
            raise Errors.OutsideContext(f'Set "{attr}" is not working because you are outside the context')
        request_context = self._get_current_request_context()
        request_context.data[attr] = value

    def setdefault_attr(self, attr: str, value: Any):
        """
        The setdefault_request_context_value() method returns the value of the item with the specified attr.
        If the attr does not exist, insert the attr, with the specified value
        """
        if not self.is_under_request_context():
            raise Errors.OutsideContext(f'Set "{attr}" is not working because you are outside the context')

        request_context = self._get_current_request_context()
        return request_context.data.setdefault(attr, value)

    def delete_attr(self, attr: str):
        if not self.is_under_request_context():
            raise Errors.OutsideContext(f'Delete "{attr}" is not working because you are outside the context')
        request_context = self._get_current_request_context()
        request_context.data.pop(attr, None)

    def get_attr(self, attr: str, default: Any = UNDEFINED, allow_outside_context=False):
        if not self.is_under_request_context():
            if not allow_outside_context:
                raise Errors.OutsideContext(f'Get "{attr}" is not working because you are outside context')
            if default is UNDEFINED:
                raise Errors.AttrNotFound(f'attr "{attr}" not found')
            return default

        value = self._get_current_request_context().data.get(attr, default)
        if value is UNDEFINED:
            raise Errors.AttrNotFound(f'attr "{attr}" not found')
        return value


class RequestContextAttr:
    def __init__(self, attr: str, request_context_mgr: RequestContextManager):
        self._attr = attr
        self._request_context_mgr = request_context_mgr

    def get(self, default=UNDEFINED, allow_outside_context=False):
        return self._request_context_mgr.get_attr(self._attr, default, allow_outside_context)

    def set(self, value):
        return self._request_context_mgr.set_attr(self._attr, value)

    def delete(self):
        return self._request_context_mgr.delete_attr(self._attr)

    def setdefault(self, value):
        return self._request_context_mgr.setdefault_attr(self._attr, value)


__version__ = "0.0.3"
