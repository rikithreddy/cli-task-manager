'''
Setup file for cli-task-manager installs all dependencies 
and converts application in to a command.
'''
from setuptools import setup

setup(
	name="cli-task",
	version=1.0,
	py_modules=['hello'],
	install_requires=['Click'],
	entry_points='''
		[console_scripts]
		clitask=clitask:main
		'''
	)