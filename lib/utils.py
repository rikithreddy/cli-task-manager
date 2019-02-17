import os
from lib.constants import *
# The function initialises all the nessessary directories required by the application
def init():
	if not os.path.exists(BASE_DIR):
		os.makedirs(BASE_DIR)

	if not os.path.exists(DATA_DIR):
		os.makedirs(DATA_DIR)

	if not os.path.exists(CONFIG_DIR):
		os.makedirs(CONFIG_DIR)

	create_task_datafile()

# Creates a the data file required by the application
def create_task_datafile():
	headers = get_data_column_list()
	if not os.path.exists(DATA_FILE):
		datafile = open(DATA_FILE, 'w')
		columns = ','.join(headers)
		datafile.write(columns)



# Return list of columns required by the datafile
def get_data_column_list():
	return [
		'id',
		'creation_time',
		'priority',
		'status',
		'estimate',
		'blocks',
		'alias',
		'deadline',
		'description',
		'type',
		]
