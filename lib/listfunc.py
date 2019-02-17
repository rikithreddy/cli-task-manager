import pandas as pd
import click
from constants import *


# Loads and returns the user datafile
def fetch_datafile():
	df = pd.read_csv(DATA_FILE)
	return df

def list_all():
	df = fetch_datafile()

	if len(df) == 0:
		click.echo("You dont have any such tasks as of now use add option to add tasks!!")
	else:
		print(df)