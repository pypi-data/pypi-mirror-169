"""Get token helper function. Retrieves the keycloak token on local machine."""
import json
import os
from sys import platform


if platform in ("linux", "darwin"):
    import pwd

from typing import Union


def get_token() -> Union[str, None]:
    """Retrieves token if it exists or returns None if no token exists."""
    if platform in ("linux", "darwin"):
        username = pwd.getpwuid(os.getuid())[0]
    elif platform == "windows":
        username = os.getlogin()
    else:
        raise Exception("Unknown platform. The CLI only supports Unix and Windows based platforms.")

    if platform in ("darwin", "linux"):
        config_filepath = rf"/Users/{username}/.dapla_cli_keycloak_token.json"
    else:
        config_filepath = rf"C:\Users\{username}\AppData\dapla_cli\dapla_cli_keycloak_token.json"

    if os.path.isfile(config_filepath):
        with open(config_filepath, encoding="UTF-8") as f:
            data = json.loads(f.read())
            keycloak_token = data["keycloak_token"]
    else:
        return None

    return str(keycloak_token)
