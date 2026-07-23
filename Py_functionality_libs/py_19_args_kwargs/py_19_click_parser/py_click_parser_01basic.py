import click

# example of command to run: python .\py_click_parser_01basic.py --age=19


@click.command()
@click.option("--name", default="not indicated")
@click.option("--age", default="not indicated")
def info_about_person(name, age):
    print(f"User: {name}, age: {age}")


if __name__ == "__main__":
    info_about_person()
