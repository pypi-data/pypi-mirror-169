# pytrutankless

Python interface for TRUTANKLESS branded water heaters

## Installation

```
pip install pytrutankless
```

## Usage

In order to obtain an auth token, a TruTanklessApi object must be instantiated and `api.authenticate` called.

```python
from pytrutankles.api import TruTanklessApiInterface(user, passwd, token[Optional])

email = "your@email.here"
password = "yoursecrethere"

api = await TruTanklessApiInterface(user=email, passwd=password)
auth = api.authenticate()
```

A Token object with the following parameters is returned;

```json
{
  "access_token": "str",
  "token_type": "str",
  "expires_in": "int",
  "expires_at": "datetime",
  "refresh_token": "str",
  "user_id": "str"
}
```

If a `Token` object is provided, it will be used for authentification unless expired. If the given `Token` is expired, a new one is retrieved from the API.

### Methods

### `authenticate()`

```
api.authenticate()
retun Token
```

Logs into service and retrieves `access_token`.

### `get_devices()`

```
api.get_devices()
```

Updates dictionaries of locations and devices.
Returns a dict of location(s) that are stored in `api._locations` and a dict of device(s) stored in `api.devices`.

### `refresh_device(device_id)`

```
api.refresh_device(device_id)
```

Given `device_id`, updates usage data for that device.
