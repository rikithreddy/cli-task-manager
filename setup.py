'''
Setup file for cli-task-manager installs all dependencies 
and converts application in to a command.
'''
from setuptools import setup

setup(
	name="cli-task",
	version=1.0,
	install_requires=['Click', 'pandas', 'numpy'],
	entry_points='''
		[console_scripts]
		clitask=clitask:main
		'''
	)
