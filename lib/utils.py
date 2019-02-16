from os import mkdir, path, makedirs, utime
BASE_DIR = "clitask/"
DATA_DIR = path.join(BASE_DIR , 'data')
CONFIG_DIR = path.join(BASE_DIR , 'config')
DATA_FILE = path.join(DATA_DIR , 'task.csv')

def init():
	if not path.exists(BASE_DIR):
		makedirs(BASE_DIR)

	if not path.exists(DATA_DIR):
		makedirs(DATA_DIR)

	if not path.exists(CONFIG_DIR):
		makedirs(CONFIG_DIR)

	open(DATA_FILE, 'a').close()
