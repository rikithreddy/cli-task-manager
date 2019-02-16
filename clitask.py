import click
from lib import utils

@click.group()
def main():
	utils.init()
	pass
@main.command()


def add():
	click.echo("Add command")


@main.command()
def list(list):
	if list:
		click.echo("You dont have any entries as of now :)")
	click.echo("List command")


@main.command()
def edit():
	click.echo("Edit command")


if __name__ == '__main__':
	main()