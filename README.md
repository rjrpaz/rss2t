# python-project-template

This is a template for new python projects according to best practices and recommendation from different sources:

- *.gitignore* is proposed from GitHub for python projects
- *LICENSE.md* is proposed from GitHub for MIT license
- Introducing "Dead Simple Python": [https://dev.to/codemouse92/introducing-dead-simple-python-563o](https://dev.to/codemouse92/introducing-dead-simple-python-563o)

**I strongly suggest to read the "Dead Simple Python" guide for more comprehensive justification on every topic (don't miss the comments also). This should be considered just as "notes" from that article.**

To mirroring this repository into a new python project, do as following:

1. Create new project on github:

    Following this example, the new project name is "new-repository".

1. Create a bare clone of the repository:

    ```bash
    git clone --bare https://github.com/rjrpaz/python-project-template.git
    ```

1. Mirror-push to the new repository:

    ```bash
    cd python-project-template.git
    git push --mirror https://github.com/rjrpaz/new-repository.git
    ```

1. Remove the temporary local repository you created earlier:

    ```bash
    cd ..
    rm -rf python-project-template.git
    ```

## Main topics to be considered in the project

These are the main aspects to be considered according to best practices.

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

You can also manually create a *requirements.txt* file with the list of packages and then install them like this:

```bash
pip install -r requirements.txt
```

or you can create the *requirements.txt* file automatically, running this from the virtual environment:

```bash
pip freeze > requirements.txt
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

A package can contain other packages. Thus, we can call our top-level directory as the main package and all the packages underneath as subpackages. If a subdirectory don't include "__init__.py", it should not be considered a package.

Another special file in the top-level package is "__main__.py". This is the file that is run when we execute our top-level package directly via *python -m pyproject*.

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

According to this example, the content of "__main__.py" file is something like this:

```console
from pyproject import app

if __name__ == '__main__':
    app.run()
```

Also, "app.py" includes the following at the bottom of the file:

```console
if __name__ == '__main__':
    run()
```

This way we can run *python -m pyproject.app* and we get the same results as *python -m pyproject*

## Data Typing and Immutability

Most important characteristics for variables in python are:

- Dynamically typed: the data type of a variable (object) is determined at run time.

- Strongly typed: once the variable is assigned, the language has strict rules about what you can do to different data types.

to get the data type from a variable we can use:

```console
if type(netWorth) is float:
    swimInMoneyBin()
```

or this will be better:

```console
if isinstance(netWorth, float):
    swimInMoneyBin()
```

Also, remember that *is* and *==* do not do the same thing. The *is* operator checks to see if the two operands are the **same instance**. On the other hand, *==* (among others) should be used for comparing **values**.

### Strings

We can wrap a literal in single quotes '...', double quotes "...", or triple quotes """...""". In Python, single-quoted strings and double-quoted strings are the same. Pick one and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.

We could use triple quotes (""") if we have both, single and double characters in the string. Also, triple quotes are multiline. Everything, including newlines and leading whitespace, is literal in triple quotes. The only exception is if we escape something using a backslash (\).

The other special use of triple quotes is in creating *docstrings*, which provide basic documentation for modules, classes, and functions.

```console
def swimInMoney():
    """
    If you're not Scrooge McDuck, please don't try this.
    Gold hurts when you fall into it from forty feet.
    """
    pass

 ...

# This text can be accessed using
print(swimInMoney.__doc__)
```

### Special String Types

*Raw strings* are preceded with an r, such as...

```console
print(r"I love backslashes: \ Aren't they cool?")
```

In a raw string, the backslash is treated like a literal character. Nothing can be "escaped" inside of a raw string. This is particularly useful for **regular expression patterns**.

The other "type" of string is a *formatted string*, or f-string. It allows you to insert the values of variables into a string in a very pretty way, without having to bother with concatenation or conversion.

```console
netWorth = 52348493767.50
richestDuck = "Scrooge McDuck"
print(f"{richestDuck} has a net worth of ${netWorth}.")
```

### Functions

Suppose we have this function:

```console
def grapplingHook(direction: float, angle: float, battleCry: str = ""):
    print(f"Direction = {direction}, Angle = {angle}, Battle Cry = {battleCry}")

grapplingHook(angle=90, direction=43.7)
```

A typical use of the function should be like this:

```console
grapplingHook(43.7, 90, "")
```

However, if we want, we can actually specify which argument we're passing which values to. This makes our code more readable in many cases:

```console
grapplingHook(angle=90, direction=43.7)
```

Also note the default value for variable *battleCry*, just is case we don't provide the value when we call the function.

It's pretty common to use None as a default value, so you can then check if the argument has a value specified, like this...

```console
def grapplingHook(direction, angle, battleCry = None):
    if battleCry:
        print(battleCry)
```

We can use *type hints* to suggest inputs and returned data types, like this:

```console
def grapplingHook(direction: float, angle: float, battleCry: str = "") -> None:
```

however this will not throw an error if the provided type is not the one explicitly listed. Is mostly used for documentation.

Also you can use a return from the function. You can call return with no arguments (*None*) or return a variable. If return is never called, then the function implicitly calls return at the end of the function cycle.

## Classes

Consider this piece of code as an example:

```console
class Starship(object):

    sound = "Vrrrrrrrrrrrrrrrrrrrrr"

    def __init__(self):
        self.engines = False
        self.engine_speed = 0
        self.shields = True

    def engage(self):
        self.engines = True

    def warp(self, factor):
        self.engine_speed = 2
        self.engine_speed *= factor

    @classmethod
    def make_sound(cls):
        print(cls.sound)
```

Better define a class like this:

```console
class Starship(object):
```

Method:

```console
def warp(self, factor):
```

We pass self as the first parameters to every single method. An exception to this are *class methods*:

```console
@classmethod
def make_sound(cls):
```

A class method is one that is shared between all instances of the class (objects). A class method never touches member variables or regular methods.

We always access member variables in a class via the dot operator *self.*. We can't do that in a class method, and that's why we call the first argument *cls*. In a class method Python passes the class to that argument instead of the object. For a class method, we also MUST put the decorator *@classmethod* on the line just above our function declaration.

Those methods from the example get called something like this:

```console
# Create our object from the starship class
uss_enterprise = Starship()

# Note, we aren't passing anything to 'self'. Python does that implicitly.
uss_enterprise.warp(4)

# We can call class functions on the object ...
uss_enterprise.make_sound()

# ... or directly on the class.
Starship.make_sound()
```

You can also define static methods with the decorator *@staticmethod* like this:

```console
@staticmethod
def beep():
    print("Beep boop beep")
```

A static method doesn't access any of the class members; it doesn't even care that it's part of the class, and that's why it doesn't need the cls argument.

Every Python class needs to have one, and only one, __init__(self) function. This is called the initializer. If you don't really need it, just define one empty (*pass*). The initializer is responsible for initializing the instance variables.

In Python, our classes can have *instance variables*, which are unique to our object (instance), and *class variables (a.k.a. static variables)*, which belong to the class, and are shared between all instances. Using the same name for this two types of variables can be a source of error because when accessing a variable on the object, the instance variables can hide the class variables, making it behave not as we expect. You should *always* declare all your instance variables in the initializer, just to prevent something weird from happening, like a function attempting to access a variable that doesn't yet exist.

There are no *private* scope for variables. There are however the chance of using an underscore in from of the variable name as a word of caution for anyone using the class, to not mess around with that variable.

Anyway, if we positively know that a variable should ever be modified outside of the class, we can add two underscores. This does *name mangling*: it changes the name of the variable, adding a single underscore and the name of the class on the front. According to the example, if we were to change *self.shields* to *self.__shields*, it would be name mangled to *self._Starship__shields*.

In Python, we can use *properties* the same way as *getters* and *setters* in Java. Properties are defined simply by preceding a method with *@property*. You can make a method look like an instance variable. Also, you can use the *@name_of_the_method.setter* as a setter. This is an example:

```console
class Starship:
    def __init__(self):
        # snip
        self._captain = "Jean-Luc Picard"

    @property
    def captain(self):
        return self._captain

    @captain.setter
    def captain(self, value):
        print("What do you think this is, " + value + ", the USS Pegasus? Back to work!")
```

```console
uss_enterprise = Starship()
uss_enterprise.captain
>>> 'Jean-Luc Picard'
uss_enterprise.captain = "Wesley"
>>> What do you think this is, Wesley, the USS Pegasus? Back to work!
```

this way you can use the method like a variable and assign values to it.

### Inheritance

When we create a class, we are inheriting from Python *object* class:

```console
class Starship(object):
```

we can inherit from our own classes this way:

```console
class USSDiscovery(Starship):

    def __init__(self):
        super().__init__()
        self.spore_drive = True
        self._captain = "Gabriel Lorca"
```

The *super().__init__()* line refers to the class we inherited from (in this case, Starship), and calls its initializer. We need to call this, so USSDiscovery has all the same instance variables as Starship.

## Errors

When an error is present in runtime, we get a *traceback*. It is recommended to read this traces bottom to top, as the last info being the most useful to find the source of the error.

You can get exceptions from code like this:

```console
try:
    code = int(input("Enter security protocol code: "))
except ValueError:
    code = 0
initiate_security_protocol(code)
```

## Next

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
