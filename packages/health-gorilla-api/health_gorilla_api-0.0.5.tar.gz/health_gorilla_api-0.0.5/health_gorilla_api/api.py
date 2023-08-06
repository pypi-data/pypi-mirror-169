import os
import datetime
import json
import requests
import jwt
from urllib import parse

TOKEN_URL = os.getenv("TOKEN_URL")
GRANT_TYPE = os.getenv("GRANT_TYPE")
CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_ID = os.getenv("SECRET_ID")
ISSUER = os.getenv("ISSUER")
SUB = os.getenv("SUB")
ASSERTION_EXPIRES_AT_MINUTES = int(os.getenv("ASSERTION_EXPIRES_AT_MINUTES"))

def get_assertion():
    now = datetime.datetime.now(tz=datetime.timezone.utc)

    assertion_expires_at = now + datetime.timedelta(minutes=ASSERTION_EXPIRES_AT_MINUTES)

    assertion = jwt.encode({
        "aud": TOKEN_URL,
        "iss": ISSUER,
        "sub": SUB,
        "iat": now.timestamp(),
        "exp": assertion_expires_at.timestamp()
    }, SECRET_ID, algorithm="HS256")

    return assertion


def get_access_token(scope, grant_type=None):
    if grant_type is None:
        grant_type = GRANT_TYPE

    payload_params = {
        "grant_type": grant_type,
        "client_id": CLIENT_ID,
        "scope": scope,
        "assertion": get_assertion()
    }
    payload = parse.urlencode(payload_params)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    print(payload_params)
    print(headers)
    print(TOKEN_URL)
    print(payload)
    response = requests.request("POST", TOKEN_URL, headers=headers, data=payload)
    print(response)
    # access_token = json.loads(response.text)

    # return access_token
