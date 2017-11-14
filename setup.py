import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pdu_ussd_converter",
    version="0.1",
    author="Saviour Gidi",
    author_email="profsaviour@gmail.com",
    description=("An to convert between pdu, gsm, ussd and string formats,\
                 document, and publish to the cheese shop a5 pypi.org."),
    license="MIT",
    keywords="PDU USSD GSM",
    url="https://github.com/saviour123/PDU-USSDConverter.git",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    install_requires=['pdu_gsm_converter'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
