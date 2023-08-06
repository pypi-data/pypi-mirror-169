# Request Context Manager
## Purpose of Request Context
When application begins handling request, request context manager create a request context. Within request context, you could access the attributes bound with the context. If you try to access attributes outside the context, OutsideContext exception will be raised. 

## How to Create Request Context Manager
```python
from request_context_manager import RequestContextManager
from request_context_manager import RequestContextAttr

# create request context manager
your_request_context_manager = RequestContextManager('your_request_context_manager_name')

# bind request context attribute
class YourRequestContextAttr:
    _request_context_manager = your_request_context_manager

    your_attr = RequestContextAttr('your_attr_name', _request_context_manager)

# get/set request context attribute within request context
with your_request_context_manager.under_request_context():
    YourRequestContextAttr.your_attr.set("hello world")
    your_attr_value = YourRequestContextAttr.your_attr.get() # "hello world"
```
