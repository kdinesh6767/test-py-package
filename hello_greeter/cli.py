"""
CLI entry point — so the package also works as a command-line tool.

After pip install, user can run:
    hello-greet --name Alice --lang fr --api-key my-key
"""
import argparse

from .config import GreeterConfig
from .greeter import Greeter


def main():
    parser = argparse.ArgumentParser(description="Hello Greeter CLI")
    parser.add_argument("--name", default="World", help="Who to greet")
    parser.add_argument("--lang", default="en", help="Language: en, es, fr, de, ja, hi, ta")
    parser.add_argument("--api-key", required=True, help="Your API key")
    parser.add_argument("--loud", action="store_true", help="SHOUT the greeting")
    args = parser.parse_args()

    config = GreeterConfig(
        api_key=args.api_key,
        name=args.name,
        language=args.lang,
        loud=args.loud,
    )

    g = Greeter(config)
    print(g.greet())


if __name__ == "__main__":
    main()
