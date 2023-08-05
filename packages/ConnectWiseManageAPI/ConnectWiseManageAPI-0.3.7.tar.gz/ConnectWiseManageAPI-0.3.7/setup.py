from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.3.7'
DESCRIPTION = 'CWManageAPI Python Wrapper'
LONG_DESCRIPTION = 'Python wrapper for CWManageAPI'

# Setting up
setup(
    name="ConnectWiseManageAPI",
    version=VERSION,
    author="lillevikit",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=['ConnectWiseManageAPI'],
    install_requires=find_packages(),
    keywords=['python', 'API', 'ConnectWise', 'Manage', 'CWManage'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)