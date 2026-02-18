"""
CLI entry point — so the package also works as a command-line tool.

After pip install, user can run:
    hello-greet --name Alice --lang fr
    (api_key is read from GREETER_API_KEY in .env)
"""
import argparse

from .config import GreeterConfig
from .greeter import Greeter


def main():
    parser = argparse.ArgumentParser(description="Hello Greeter CLI")
    parser.add_argument("--name", default=None, help="Who to greet (or set GREETER_NAME)")
    parser.add_argument("--lang", default=None, help="Language: en, es, fr, de, ja, hi, ta (or set GREETER_LANGUAGE)")
    parser.add_argument("--api-key", default=None, help="Your API key (or set GREETER_API_KEY in .env)")
    parser.add_argument("--loud", action="store_true", default=None, help="SHOUT the greeting (or set GREETER_LOUD)")
    args = parser.parse_args()

    kwargs = {}
    if args.api_key is not None:
        kwargs["api_key"] = args.api_key
    if args.name is not None:
        kwargs["name"] = args.name
    if args.lang is not None:
        kwargs["language"] = args.lang
    if args.loud is not None:
        kwargs["loud"] = args.loud

    config = GreeterConfig(**kwargs)
    g = Greeter(config)
    print(g.greet())


if __name__ == "__main__":
    main()
