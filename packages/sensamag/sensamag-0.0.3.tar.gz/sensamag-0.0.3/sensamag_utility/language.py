import mariadb
from rich import print

from sensamag_utility.utility import print_as_table


def list_languages(conn: mariadb.Connection):
    print("> Fetching languages table")
    cur = conn.cursor()
    try:
        cur.execute(
            """
        SELECT * FROM localizationlanguages
        """
        )
        print_as_table(cur, name="localizationlanguages")
        print(f"> [bold green]Fetched: {cur.affected_rows} rows")
    except mariadb.Error as exception:
        print(f"> [bold red]Error fetching languages:[/] {exception}")


def add_language(conn: mariadb.Connection, name: str, culture: str, priority: int):
    print(
        f"""
    > Adding new language:
    | > name: {name}
    | > culture: {culture}
    | > priority: {priority}
    """
    )
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO localizationlanguages (Name,Culture, Priority) VALUES (?, ?, ?)",
            (name, culture, priority),
        )
        conn.commit()
        print(
            f"> [bold green]Language {name} is added successfully with {cur.lastrowid} id"
        )
    except mariadb.Error as exception:
        print(f"> [bold red]Error adding new language[/]: {exception}")


def remove_language(conn: mariadb.Connection, lang_id: int):
    print(f"> Removing language by id: {lang_id}")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM localizationlanguages WHERE Id = (?)", (lang_id,))
        conn.commit()
        print(f"> [bold green]Language with id: {lang_id} is removed successfully!")
    except mariadb.Error as exception:
        print(f"> [bold red]Error removing language:[/] {exception}")
