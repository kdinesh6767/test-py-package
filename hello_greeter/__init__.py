"""
hello-greeter SDK — A simple example of a pip-installable Python package.

Install from GitHub::

    pip install git+https://github.com/<org>/hello-world.git

Quick start — create a .env file on your machine::

    GREETER_API_KEY=my-secret-key
    GREETER_NAME=Alice
    GREETER_LANGUAGE=fr

Then::

    from hello_greeter import Greeter
    g = Greeter()
    print(g.greet())  # "Bonjour, Alice!"
"""

__version__ = "1.0.0"

from .config import GreeterConfig
from .greeter import Greeter

__all__ = ["Greeter", "GreeterConfig"]
