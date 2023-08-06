[![flake8 Lint](https://github.com/acdh-oeaw/acdh-handle-pyutils/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-handle-pyutils/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/acdh-handle-pyutils/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-handle-pyutils/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/acdh-handle-pyutils/branch/master/graph/badge.svg?token=96XqlDbpDw)](https://codecov.io/gh/acdh-oeaw/acdh-handle-pyutils)
[![PyPI version](https://badge.fury.io/py/acdh-handle-pyutils.svg)](https://badge.fury.io/py/acdh-handle-pyutils)

# acdh-handle-pyutils

Utility functions to interact with handle.net API

## install

`pip install acdh-handle-pyutils`


## how to use

see `./tests/test_client.py` and also checkout the provided defaults for `acdh_handle_pyutils.client.HandleClient` 

### register handle for url

```Python
import os
from acdh_handle_pyutils.client import HandleClient


HANDLE_USERNAME = os.environ.get("HANDLE_USERNAME")
HANDLE_PASSWORD = os.environ.get("HANDLE_PASSWORD")
URL_TO_REGISTER = "https://id.hansi4ever.com/123"

cl = HandleClient(HANDLE_USERNAME, HANDLE_PASSWORD)
result = cl.register_handle(URL_TO_REGISTER, full_url=True)
print(result)
# https://hdl.handle.net/21.11115/0000-000F-743B-D
```

Be aware that it might take a while until the registerd handle resolves

### update handle


```Python
import os
from acdh_handle_pyutils.client import HandleClient


HANDLE_USERNAME = os.environ.get("HANDLE_USERNAME")
HANDLE_PASSWORD = os.environ.get("HANDLE_PASSWORD")
HANDLE_TO_UPDATE = "https://hdl.handle.net/21.11115/0000-000F-743B-D"
URL_TO_UPDATE = "https://sumsi.com/is-the-best"


cl = HandleClient(HANDLE_USERNAME, HANDLE_PASSWORD)
updated = cl.update_handle(HANDLE_TO_UPDATE, URL_TO_UPDATE)print(result)

print(updated.status_code) # should return for `204 No Content` HTTP response code for a successful update
# 204
```

Be aware that it might take until the handle is actually updated by the handle service provider

