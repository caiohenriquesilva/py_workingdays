import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_workingdays",
    version="0.0.6",
    author="Caio Henrique Silva",
    author_email="caio@caiowd.me",
    description="This is a python lib to deal with working days with support for localization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caiohenriquesilva/pyworkingdays",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
