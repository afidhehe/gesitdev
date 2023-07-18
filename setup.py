from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gesitdev/__init__.py
from gesitdev import __version__ as version

setup(
	name="gesitdev",
	version=version,
	description="for development purpose",
	author="gesitERP.com",
	author_email="support@gesitERP.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
