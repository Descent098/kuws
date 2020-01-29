# Welcome to the KUWS documentation!



## what is kuws?

Kuws is a utility I wrote with the intention of implementing some common web scripts into one cohesive library. it is primarily intended to be used as a standalone script, but it can also be used as an API. 



## Installation

### From PyPi

run ```pip install kuws``` or ```sudo pip3 install kuws```.



### From source

1. Clone the github repo ([https://github.com/Descent098/kuws](https://github.com/Descent098/kuws))
2. cd into the 'kuws' root directory (where setup.py is) and run ```pip install .``` or ```sudo pip3 install . ```



You can validate it is installed properly by typing ```kuws``` into your terminal, the output should look like this:

```bash
Kieran's Useful Web Scripts; A set of python web utility scripts.

Usage:
    kuws [-h] [-v]
    kuws redirects <url> [-t]
    kuws youtube <url> [<path>]
    kuws ssl <hostname> [-e] [-c]

Options:
    -h --help               Show this help message and exit
    -v --version            Show program's version number and exit
    -e --expiry             If specified will check the expiry of ssl cert/domain
    -c --cert               If specified will print the full details of the SSL cert
    -t --trace              If specified will show the full trace of the provided url
```

