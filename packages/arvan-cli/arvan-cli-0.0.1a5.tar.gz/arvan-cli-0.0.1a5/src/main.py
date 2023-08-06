from typing import List, Optional
import typer
from src.auth import Auth
from src.client import ArvanClient

app = typer.Typer()


@app.command()
def authenticate(
    api_key: str = typer.Option(..., prompt=True, hide_input=True,
                                help="Set your API key. Keep in mind that it will be stored in plain text."),
):
    """
    Add API key
    """
    Auth.create(api_key)


@app.command()
def ls():
    """
    List all servers
    """
    if not Auth.exists():
        typer.echo("You need to authenticate first.")
        return
    client = ArvanClient(Auth.get())
    servers = client.get_all_servers()
    import json
    typer.echo(json.dumps(servers, indent=4))


@app.command()
def turn_on(
    all: bool = typer.Option(False, "--all", "-a",
                             help="Turn on all servers"),
    name: Optional[str] = typer.Option(None, "--name", "-n",
                                       metavar="NAME",
                                       help="Turn on server by name"),
) -> None:
    """
    Turn on server(s)
    """
    if not Auth.exists():
        typer.echo("You need to authenticate first.")
        return
    client = ArvanClient(Auth.get())
    if all:
        typer.echo("Turning on all servers")
        client.turn_on_all_servers()
        typer.echo("Done")
        return
    if name:
        typer.echo(f"Turning on {name}")
        client.turn_on_server_by_name(name)
        typer.echo("Done")
        return
    typer.echo("Wrong usage. Use 'arvan turn-on --help` for more information.")


@app.command()
def shutdown(
    all: bool = typer.Option(False, "--all", "-a",
                             help="Shutdown all servers"),
    name: Optional[str] = typer.Option(None, "--name", "-n",
                                       metavar="NAME",
                                       help="Shutdown server by name"),
) -> None:
    """
    Shutdown server(s)
    """
    if not Auth.exists():
        typer.echo("You need to authenticate first.")
        return
    client = ArvanClient(Auth.get())
    if all:
        typer.echo("Shutting down all servers")
        client.shutdown_all_servers()
        typer.echo("Done")
        return
    if name:
        typer.echo(f"Shutting down {name}")
        client.shutdown_server_by_name(name)
        typer.echo("Done")
        return
    typer.echo("Wrong usage. Use 'arvan shutdown --help` for more information.")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
