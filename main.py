from BOT.table import table
from BOT.bot import start


def run():
    services = table()
    start(services)


if __name__ == "__main__":
    run()
