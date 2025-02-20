import os
from setuptools import setup, find_packages

PACKAGE = "webullpaysdkdemos"
DESCRIPTION = "The demos of Webullpay Python SDK."
TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__
AUTHOR = "Webullpay"
AUTHOR_EMAIL = ""
URL = ""
RD_CONTENT_TYPE = "text/markdown"
LICENSE = "Apache License 2.0"

with open("README.rst") as fp:
    LONG_DESCRIPTION = fp.read()

requires = [
    "webullpay-python-sdk-mdata==0.1.0",
    "webullpay-python-sdk-trade==0.1.0"
]

setup_args = {
    'version': VERSION,
    'author': AUTHOR,
    'author_email': AUTHOR_EMAIL,
    'description': DESCRIPTION,
    'long_description_content_type': RD_CONTENT_TYPE,
    'license': LICENSE,
    'url': URL,
    'packages': find_packages(exclude=["tests*"]),
    'package_data': {},
    'platforms': 'any',
    'install_requires': requires
}

setup(name='webullpay-python-sdk-demos', **setup_args)
