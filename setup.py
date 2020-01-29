"""Contains all the configuration for the package on pypi/pip.

Functions
---------
concat_description : str
    Reads and yields the content of the filenames.

Module Variables
----------------
long_description : str
    The content in README.md and CHANGELOG.md and used for module description.

Notes
-----
Primary entrypoint is in kuws.command_line_utility.

"""
import setuptools

def get_content(*filename):
    """ Gets the content of a file and returns it as a string
    Args:
        filename(str): Name of file to pull content from
    Returns:
        str: Content from file
    """
    content = ""
    for file in filename:
        with open(file, "r") as full_description:
            content += full_description.read()
    return content


setuptools.setup(
    name="kuws",
    version="0.0.6",
    author="Kieran Wood",
    author_email="kieran@canadiancoding.ca",
    description="A set of python scripts for common web tasks",
    long_description = get_content("README.md", "CHANGELOG.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/Descent098/kuws",
    packages=setuptools.find_packages(),
    entry_points={
          'console_scripts': ['kuws = kuws.command_line_utility:main']
      },
    install_requires=[
    "requests",
    "pytube3",
    "docopt",
      ],
    extras_require = {
        "dev" : ["nox",    # Used to run automated processes
                 "pytest", # Used to run the test code in the tests directory
                 "mkdocs"],# Used to create HTML versions of the markdown docs in the docs directory

    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)