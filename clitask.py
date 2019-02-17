import click
from lib import utils, listfunc
@click.group()
def main():
	utils.init()
	pass
@main.command()


def add():
	click.echo("Add command")


@main.command()
def list():
	listfunc.list_all()

@main.command()
def edit():
	click.echo("Edit command")


if __name__ == '__main__':
	main()