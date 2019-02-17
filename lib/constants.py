import os 

# Global constants required for the application
USER_HOME = os.getenv("HOME")
BASE_DIR = os.path.join(USER_HOME, '.clitask')
DATA_DIR = os.path.join(BASE_DIR , 'data')
CONFIG_DIR = os.path.join(BASE_DIR , 'config')
DATA_FILE = os.path.join(DATA_DIR , 'task.csv')

