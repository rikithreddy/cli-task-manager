import click
from lib import utils

@click.group()
def run():
	utils.init()
	pass
@run.command()

def add():
	click.echo("Add command")


@run.command()
def list():
	click.echo("List command")



@run.command()
def edit():
	click.echo("Edit command")


if __name__ == '__main__':
	run()