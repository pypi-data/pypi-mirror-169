from setuptools import setup, find_packages
import codecs
import os


# Setting up
setup(
    name="SdaMyPrimPackage",
    version='4.3.1',
    author="Guido Xhindoli",
    author_email="<mail@gmail.com>",
    description='A package that prints PRIM numbers',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['pythonsdaal', 'SdaMyPrimPackage', 'prim', 'prim  numbers', 'sda', 'SDA'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)