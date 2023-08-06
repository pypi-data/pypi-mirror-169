import typer
from typer import Typer

from sensamag_utility import exporter, language
from sensamag_utility.connection_manager import ConnectionManager

app = Typer(no_args_is_help=True)
connection_manager = ConnectionManager()


@app.callback(invoke_without_command=True)
def connection(
    user: str = None,
    password: str = None,
    host: str = None,
    port: int = None,
    database: str = None,
    reset: bool = False,
):
    if reset:
        connection_manager.reset_connection()
    connection_manager.set_connection(user, password, host, port, database)


@app.command()
def addlang(
    name: str = typer.Option(..., prompt=True),
    culture: str = typer.Option(..., prompt=True),
    priority: int = typer.Option(..., prompt=True),
):
    with connection_manager.get_connection() as conn:
        language.add_language(conn, name, culture, priority)


@app.command()
def removelang(lang_id: int = typer.Option(..., prompt=True)):
    with connection_manager.get_connection() as conn:
        language.remove_language(conn, lang_id)


@app.command()
def listlang():
    with connection_manager.get_connection() as conn:
        language.list_languages(conn)


@app.command()
def exportdb(path: str = typer.Option(..., prompt=True)):
    with connection_manager.get_connection() as conn:
        exporter.export_db(conn, path)
