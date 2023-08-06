import base64
import hashlib
import json
from pathlib import Path
from random import randint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

import websocket


class ObsClient:
    DELAY = 0.001

    def __init__(self, **kwargs):
        defaultkwargs = {
            **{key: None for key in ["host", "port", "password"]},
            "subs": 0,
        }
        kwargs = defaultkwargs | kwargs
        for attr, val in kwargs.items():
            setattr(self, attr, val)
        if not (self.host and self.port and self.password):
            conn = self._conn_from_toml()
            self.host = conn["host"]
            self.port = conn["port"]
            self.password = conn["password"]

        self.ws = websocket.WebSocket()
        self.ws.connect(f"ws://{self.host}:{self.port}")
        self.server_hello = json.loads(self.ws.recv())

    def _conn_from_toml(self):
        filepath = Path.cwd() / "config.toml"
        with open(filepath, "rb") as f:
            conn = tomllib.load(f)
        return conn["connection"]

    def authenticate(self):
        secret = base64.b64encode(
            hashlib.sha256(
                (
                    self.password + self.server_hello["d"]["authentication"]["salt"]
                ).encode()
            ).digest()
        )

        auth = base64.b64encode(
            hashlib.sha256(
                (
                    secret.decode()
                    + self.server_hello["d"]["authentication"]["challenge"]
                ).encode()
            ).digest()
        ).decode()

        payload = {
            "op": 1,
            "d": {
                "rpcVersion": 1,
                "authentication": auth,
                "eventSubscriptions": self.subs,
            },
        }

        self.ws.send(json.dumps(payload))
        return self.ws.recv()

    def req(self, req_type, req_data=None):
        if req_data:
            payload = {
                "op": 6,
                "d": {
                    "requestType": req_type,
                    "requestId": randint(1, 1000),
                    "requestData": req_data,
                },
            }
        else:
            payload = {
                "op": 6,
                "d": {"requestType": req_type, "requestId": randint(1, 1000)},
            }
        self.ws.send(json.dumps(payload))
        response = json.loads(self.ws.recv())
        return response["d"]
