import sys

import mariadb
from rich import print

DEFAULT_USER = "sensamag_utility"
DEFAULT_PASSWORD = "verystrongpassword"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 3308
DEFAULT_DATABASE = "sensamag_sp"


class ConnectionManager:
    def __init__(self):
        self.user = DEFAULT_USER
        self.password = DEFAULT_PASSWORD
        self.host = DEFAULT_HOST
        self.port = DEFAULT_PORT
        self.database = DEFAULT_DATABASE

    def reset_connection(self):
        self.user = DEFAULT_USER
        self.password = DEFAULT_PASSWORD
        self.host = DEFAULT_HOST
        self.port = DEFAULT_PORT
        self.database = DEFAULT_DATABASE
        print("> [bold yellow]Connection parameters reset to default!")

    def set_connection(
        self,
        user: str = None,
        password: str = None,
        host: str = None,
        port: int = None,
        database: str = None,
    ):
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if database is not None:
            self.database = database
        print("> [bold yellow]New connection parameters:")
        self.print_params()

    def print_params(self):
        print(
            f"""
        | > User: {self.user}
        | > Password: {self.password}
        | > Host: {self.host}
        | > Port: {self.port}
        | > Database: {self.database}
        """
        )

    def get_connection(self):
        try:
            conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database,
            )
            print("> [bold green]Connected successfully!")
            return conn
        except mariadb.Error as exception:
            print(f"> [bold red]Error connecting to MariaDB[/]: {exception}")
            sys.exit(1)
