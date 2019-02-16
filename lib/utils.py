from os import mkdir, path, makedirs
import os

# Global constants required for the application

USER_HOME = os.getenv("HOME")
BASE_DIR = os.path.join(USER_HOME, '.clitask')
DATA_DIR = os.path.join(BASE_DIR , 'data')
CONFIG_DIR = os.path.join(BASE_DIR , 'config')
DATA_FILE = os.path.join(DATA_DIR , 'task.csv')


# The function initialises all the nessessary directories required by the application
def init():
	if not path.exists(BASE_DIR):
		os.makedirs(BASE_DIR)

	if not path.exists(DATA_DIR):
		os.makedirs(DATA_DIR)

	if not path.exists(CONFIG_DIR):
		os.makedirs(CONFIG_DIR)

	create_task_datafile()

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
