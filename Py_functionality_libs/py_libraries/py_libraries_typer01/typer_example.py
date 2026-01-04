import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    # Welcome the User
    print(f"Hello {name}")


@app.command()
def goodbye(
    last_name: str,
    formal: bool = False,
    excited: bool = typer.Option(False, help="Add excitement!"),
):
    # Goodbye to User
    if formal:
        message = f"Goodbye Ms./Mr. {last_name}. Have a good day"
    else:
        message = f"Bye {last_name}"
    if excited:
        message += "!!!"
    print(message)


if __name__ == "__main__":
    app()
