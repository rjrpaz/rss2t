# python-project-template

This is a template for new python projects according to best practices and recommendation from different sources:

- *.gitignore* is proposed from GitHub for python projects
- *LICENSE.md* is proposed from GitHub for MIT license
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

### Project Structure and Imports

Besides files *README.md*, *LICENSE.md* and *.gitignore*, your project must reside in a separated directory itself.

According to PEP8:

- Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.
- Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

Any Python (.py) file is a module and a bunch of modules in a directory is a package. Also, a package must include a file called __init__.py

Modules are named by filenames and packages are named by their directory name. This means that filenames should be all lowercase, with underscores if that improves readability. Similarly, directory names should be all lowercase, without underscores if at all avoidable.

This is OK:

```bash
pyproject/data/load_settings.py
```

this is NOT OK:

```console
pyproject/Data/LoadSettings.py
```

A package can contain other packages. Thus, we can call our top-level directory as the main package and all the packages underneath as subpackages. If a subdirectory don't include *__init__.py*, it should not be considered a package.

Another special file in the top-level package is *__main__.py*. This is the file that is run when we execute our top-level package directly via *python -m pyproject*.

Regarding to imports, we can use it like this:

```console
from smart_door import open, close
open()
close()
```

Just in case we are importing more that one module that includes the same methods, then we can explicitly call the functions.

We can also import stuff from our own project (using absolute or relative path):

```console
python-project-template
├── LICENSE.md
├── README.md
├── pyproject
│   ├── app.py
│   ├── common
│   │   ├── classproperty.py
│   │   ├── constants.py
│   │   ├── game_enums.py
│   │   └── __init__.py
 ...
│   ├── __init__.py
│   ├── __main__.py
│   ├── resources
 ...
```

```console
from pyproject.common.game_enums import GameMode
```

According to this example, the content of *__main__.py* file is something like this:

```console
from pyproject import app

if __name__ == '__main__':
    app.run()
```

Also, *app.py* includes the following at the bottom of the file:

```console
if __name__ == '__main__':
    run()
```

This way we can run *python -m pyproject.app* and we get the same results as *python -m pyproject*

## Next

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
