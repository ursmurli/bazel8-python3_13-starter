from typer import Typer
from calculator import Calculator
import requests

app = Typer(no_args_is_help=True)


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def bye(name: str):
    print(f"Bye {name}")

@app.command()
def sum(first: int, second: int):
    calculator = Calculator()
    result = calculator.add(first, second)
    print(f"Sum : {first} + {second} = {result}")

@app.command()
def version():
    print(requests.__version__)


# Runs the app
if __name__ == "__main__":
    app()