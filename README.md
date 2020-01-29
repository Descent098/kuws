# Kuws; Kieran's Useful Web Scripts

Some useful, and common web actions all packaged together



## Quick-start

*Include how people can get started using your project in the shortest time possible*



### Installation

#### From pypi

Run ```pip install kuws```.



#### From source

1. Clone this repo: ([https://github.com/Descent098/kuws](https://github.com/Descent098/kuws))
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory



#### Usage

#### Arguments

```bash
Kieran's Useful Web Scripts; A set of python web utility scripts.

Usage:
    kuws --version
    kuws (-h | --help)
    kuws ssl <url> [-e]
    kuws redirects <url> [-t]
    kuws domains [-k=<whoiskey>]
    kuws domains <domain> [-e] [-k=<whoiskey>]

Options:
    -h --help               Show this help message and exit
    -v --version            Show program's version number and exit
    -e --expiry             If specified will check the expiry of ssl cert/domain
    -t --trace              If specified will show the full trace of the provided url
    -k --key=<whoiskey>     If specified will register the whois domain key SEE: https://jsonwhois.io/
```



##### ssl

...



#### redirects

....



##### domains

...



## Additional Documentation

Additional Documentation can be found at [https://kuws.readthedocs.io](https://kuws.readthedocs.io).



## Development-Contribution guide

*If you have any useful information that may be pertinent to people beginning to help develop the project put it here*



### Installing development dependencies

There are a few dependencies you will need to use this package fully, they are specified in the extras require parameter in setup.py but you can install them manually:

```
nox   	# Used to run automated processes
pytest 	# Used to run the test code in the tests directory
mkdocs	# Used to create HTML versions of the markdown docs in the docs directory
```

Just go through and run ```pip install <name>``` or ```sudo pip3 install <name>```. These dependencies will help you to automate documentation creation, testing, and build + distribution (through PyPi) automation.



### Folder Structure

*A Brief explanation of how the project is set up for people trying to get into developing for it*



#### /kuws/command_line_utility.py

The main entrypoint for the kuws command.



##### /kuws/utilities

Contains all the core logic that is used by the main entrypoint.



#### /docs

*Contains markdown source files to be used with [mkdocs](https://www.mkdocs.org/) to create html/pdf documentation.* 

**Before you can use this you will need to setup the mkdocs.yml file **



#### /tests

*Contains tests to be run before release* 

**Before you can use this you will need to create tests, for more details take a look at [pytest](https://docs.pytest.org/en/latest/) **



#### Root Directory

**setup.py**: Contains all the configuration for installing the package via pip.



**LICENSE**: This file contains the licensing information about the project.



**CHANGELOG.md**: Used to create a changelog of features you add, bugs you fix etc. as you release.



**mkdocs.yml**: Used to specify how to build documentation from the source markdown files.



**noxfile.py**: Used to configure various automated processes using [nox](https://nox.readthedocs.io/en/stable/), these include;

- Building release distributions
- Releasing distributions on PyPi
- Running test suite agains a number of python versions (3.5-current)

If anything to do with deployment or releases is failing, this is likely the suspect.



There are 4 main sessions built into the noxfile and they can be run using ```nox -s <session name>``` i.e. ```nox -s test```:

- build: Creates a source distribution, builds the markdown docs to html, and creates a universal wheel distribution for PyPi.
- release: First runs the build session, then asks you to confirm all the pre-release steps have been completed, then runs *twine* to upload to PyPi
- test: Runs the tests specified in /tests using pytest, and runs it on python versions 3.5-3.8 (assuming they are installed)
- docs: Serves the docs on a local http server so you can validate they have the content you want without having to fully build them.



**.gitignore**: A preconfigured gitignore file (info on .gitignore files can be found here: https://www.atlassian.com/git/tutorials/saving-changes/gitignore)