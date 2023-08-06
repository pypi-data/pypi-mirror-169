from setuptools import find_packages, setup


setup(
	name='univisa',
	packages=find_packages(include=['univisa']),
	version='0.0.1.1',
	description='UniVISA Library',
	author='Alexander Gorbunov',
	author_email='sasha2000.gorbunov@gmail.com',
	install_requires=['pyvisa']
)

