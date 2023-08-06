import datetime
import requests
import jwt
from urllib import parse


def get_assertion(aud, sub, iss, secret_id, expire_at_minutes=10) :
    now = datetime.datetime.now(tz=datetime.timezone.utc)

    assertion_expires_at = now + datetime.timedelta(minutes=expire_at_minutes)

    assertion = jwt.encode({
        "aud": aud,
        "iss": iss,
        "sub": sub,
        "iat": now.timestamp(),
        "exp": assertion_expires_at.timestamp()
    }, secret_id, algorithm="HS256")

    return assertion


def get_access_token(scope, client_id, aud, sub, iss, secret_id, grant_type):
    payload_params = {
        "grant_type": grant_type,
        "client_id": client_id,
        "scope": scope,
        "assertion": get_assertion(aud, sub, iss, secret_id)
    }
    payload = parse.urlencode(payload_params)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    return requests.request("POST", aud, headers=headers, data=payload)
