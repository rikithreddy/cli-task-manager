'''
Setup file for cli-task-manager installs all dependencies 
and converts application in to a command.
'''
from setuptools import setup


with open("README.md") as f:
	long_desc = "f.read()"
setup(
	name="cli-task",
	description='Manage tasks',	
	author="Rikith Reddy",
	long_description=long_desc,
	author_email="rikith.legend@gmail.com",
	url="https://rikithreddy.github.io/",
	version=1.0,
	package=['lib'],
	install_requires = [
		'Click', 
		'pandas', 
		'numpy'],
	entry_points='''
		[console_scripts]
		clitask=clitask:main
		'''
	)
