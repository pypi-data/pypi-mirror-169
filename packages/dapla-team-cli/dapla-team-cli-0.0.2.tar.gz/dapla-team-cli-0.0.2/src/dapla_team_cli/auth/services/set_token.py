"""Set token helper function. Sets or updates keycloak token on local machine."""
import json
import os
from sys import platform
from typing import Union


if platform in ("linux", "darwin"):
    import pwd

import questionary as q
from rich.console import Console
from rich.style import Style


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "error": Style(color="red", blink=True, bold=True),
    "success": Style(color="green", blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
}


def set_token(keycloak_token: Union[str, None]) -> None:
    """Sets or updates a keycloak token on users local machine."""
    if platform in ("linux", "darwin"):
        username = pwd.getpwuid(os.getuid())[0]
    elif platform == "windows":
        username = os.getlogin()
    else:
        raise Exception("Unknown platform. The CLI only supports Unix and Windows based platforms.")

    if platform in ("darwin", "linux"):
        config_filepath = rf"/Users/{username}/.dapla_cli_keycloak_token.json"
    else:
        config_filepath = r"C:/windows/path/here"

    if not keycloak_token:
        keycloak_token = q.text(
            "Please provide a keycloak token. Please go to https://httpbin-fe.staging-bip-app.ssb.no/anything/bearer to fetch it:"
        ).ask()

    if not os.path.isfile(config_filepath):
        data = {"keycloak_token": keycloak_token}
        with open(config_filepath, "x", encoding="UTF-8") as f:
            json.dump(data, f)
    else:
        data = {"keycloak_token": keycloak_token}
        with open(config_filepath, "w", encoding="UTF-8") as f:
            json.dump(data, f)

    console.print("Token was succesfully added.", style=styles["success"])
