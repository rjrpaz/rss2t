# python-project-template

This is a template for new python projects according to some best practices and recommendation from different sources:

- Introducing "Dead Simple Python": [https://dev.to/codemouse92/introducing-dead-simple-python-563o](https://dev.to/codemouse92/introducing-dead-simple-python-563o)

This are the main aspect to be considered according to best practices.

## Main topics to be considered in the project

### Virtual Environments and pip

A virtual environment is a sandbox to test and run our project. We should install the required packages of our program in that sandbox.

To use a virtual environment, install *pip* and *venv*:

```bash
sudo apt install python3-venv python3-pip
```

We can create the virtual environment like this:

```bash
python3 -m venv .venv
```

This will create a *.venv* directory where the sandbox resides.

To use the virtual environment, run:

```bash
source .venv/bin/activate
```

This will change the prompt. Now we can run *pip* to install all  packages and dependencies required for our code.

You can also create a *requirements.txt* file with the list of packages and then install them like this:

```bash
pip install -r requirements.txt
```

to exit the virtual environment just run

```bash
deactivate
```

You can use the virtual environment without activating, like this:

```bash
./.venv/bin/pip search web scrapping
./.venv/bin/pip install web-downloader
./.venv/bin/python
```

It is recommended to start the code with a "she-bang" like this:

```bash
#!/usr/bin/env python3
```

instead of using the full path to the python binary.

## Next

1. Project Structure and Imports
1. Data Typing and Immutability
1. Classes
1. Errors
1. Loops and Iterators
1. Iterator Power Tools
1. List Comprehensions and Generator Expressions
1. Generators and Coroutines
1. Lambdas, Decorators, and Other Magic
1. Working with Files
1. Context Managers
1. File Formats
1. Binary
1. Async
1. Threads
1. Multiprocessing
1. Random Numbers
1. Testing
1. Debugging
1. setup.py and Packaging
1. Python Flavors: CPython vs. Pypy
