# Ubisoft Online Config Service

Web service emulating `onlineconfigservice.ubi.com`, allows for redirections to specific Ubisoft game services, including RDV authentication endpoints.

Originally reversed by [@zeroKilo](https://github.com/zeroKilo).

## Usage

Set `RDV_IP` and `RDV_PORT` for the desired RDV endpoint. Optionally adjust other service URLs if needed.

Redirect `onlineconfigservice.ubi.com` requests to this service, e.g. using `hosts` file.

Install dependencies and run:
```
pip install -r requirements.txt
python onlineconfig.py
```
