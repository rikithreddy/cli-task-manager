import click

@click.group()
def run():
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
