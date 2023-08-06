from setuptools import setup, find_packages  # noqa: H301

NAME = "rasa-vier-cvg"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "rasa-sdk",
  "cvg-python-sdk",
]

setup(
    name=NAME,
    version=VERSION,
    description="Rasa-integration for the VIER Cognitive Voice Gateway",
    author="VIER GmbH",
    author_email="support@vier.ai",
    url="https://cognitivevoice.io",
    keywords=["VIER", "VIER Cognitive Voice Gateway SDK", "Channel"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
)

