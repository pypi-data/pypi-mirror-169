from rich import print
from rich.table import Table


def print_as_table(cur: dict, name: str = "Result"):
    table = Table(*[row[0] for row in cur.description], title=name)
    for row in cur:
        table.add_row(*[str(ele) for ele in row])
    print(table)
