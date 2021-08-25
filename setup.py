from setuptools import setup

setup(
    name='pyserv',
    version='1.0',
	packages=["pyserv", "pyserv.extra", "pyserv.extra.exceptions"],
    install_requires = [x.rstrip() for s in (open("requirements.txt", "r"))]
	license='MIT',
    description='IServ API library',
    author='Veil',
    )