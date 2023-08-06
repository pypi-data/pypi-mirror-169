"""
Scripts to drop data.
"""
import mariadb
from rich import print as rprint


def drop_text_table(conn: mariadb.Connection) -> None:
    """
    Drop TextReferences and TextContents table from Database.
    :param conn: connection object
    """
    rprint("> Removing rows from textcontents and textreferences tables!")
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE textcontents; DROP TABLE textreferences;")
        conn.commit()
        rprint(
            f"> [bold green]Removed successfully [yellow]{cur.affected_rows}[/yellow] rows."
        )
    except mariadb.Error as exception:
        raise Exception(">Error dropping tables!") from exception
