
# Solar Backend.
> SolarSec web-app backend made for [Solar Security](https://solarsec.fbi.gov/) Version 0.01

## Basic Requirements
  > [**Python 3.10**](https://www.python.org/downloads/release/python-3100/),
  > [**VPS**](https://www.ovh.com/world/) <br >

## How-to use.
```python ... Webserver_port rate_limit_port debug```

## Visitor-lookup prefix
### CURL
`curl -X GET http://....:.../api/v1/script?id=...` <br >
### Python
```py
import requests,json

with requests.get("http://...:.../api/v1/scripts?id=...") as API_Reference:
    Response = json.dumps(API_Reference.text)
```
