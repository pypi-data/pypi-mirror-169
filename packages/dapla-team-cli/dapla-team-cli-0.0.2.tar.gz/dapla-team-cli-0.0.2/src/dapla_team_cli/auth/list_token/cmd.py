"""Login CLI command definition."""
import click

from dapla_team_cli.auth.services.get_token import get_token


@click.command()
def list_token() -> None:
    """Retrieves keycloak token from local machine or informs user that no such token exists."""
    keycloak_token = get_token()

    if keycloak_token:
        print(f"Your token: {keycloak_token}")
    else:
        print("You do not have a keycloak token set. Please run dpteam auth login --with-token <your_token> in order to add it.")
