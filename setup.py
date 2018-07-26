import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = '0.1.0'
__author__ = "Caio Henrique Silva"

setuptools.setup(
    name="py_workingdays",
    version=__version__,
    author=__author__,
    author_email="caio@caiowd.me",
    description="This is a python lib to deal with working days",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caiohenriquesilva/py_workingdays",
    packages=['py_workingdays'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
