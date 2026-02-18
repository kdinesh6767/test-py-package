"""
hello-greeter SDK — A simple example of a pip-installable Python package.

Install from GitHub::

    pip install git+https://github.com/<org>/hello-world.git

Usage::

    from hello_greeter import Greeter, GreeterConfig

    config = GreeterConfig(api_key="my-key", name="Alice", language="fr")
    g = Greeter(config)
    print(g.greet())  # "Bonjour, Alice!"
"""

__version__ = "1.0.0"

from .config import GreeterConfig
from .greeter import Greeter

__all__ = ["Greeter", "GreeterConfig"]
