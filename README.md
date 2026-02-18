# hello-greeter

A minimal example of a Python SDK installable via `pip install` from GitHub.

## Installation

```bash
pip install git+https://github.com/<org>/hello-world.git
```

Or from a wheel (GitHub Release):

```bash
pip install https://github.com/<org>/hello-world/releases/download/v1.0.0/hello_greeter-1.0.0-py3-none-any.whl
```

## Setup

Create a `.env` file in your project directory (the machine where the package is installed):

```env
GREETER_API_KEY=my-secret-key
GREETER_NAME=Alice
GREETER_LANGUAGE=fr
GREETER_LOUD=false
```

| Env Variable | Required | Default | Description |
|---|---|---|---|
| `GREETER_API_KEY` | Yes | — | Your API key |
| `GREETER_NAME` | No | `World` | Who to greet |
| `GREETER_LANGUAGE` | No | `en` | Language: en, es, fr, de, ja, hi, ta |
| `GREETER_LOUD` | No | `false` | Uppercase the greeting |

## SDK Usage (in Python code)

```python
from hello_greeter import Greeter

# Reads GREETER_API_KEY, GREETER_NAME, etc. from .env automatically
g = Greeter()
print(g.greet())               # "Bonjour, Alice!"
print(g.available_languages()) # ["en", "es", "fr", "de", "ja", "hi", "ta"]
```

You can also override any value explicitly:

```python
from hello_greeter import Greeter, GreeterConfig

config = GreeterConfig(api_key="my-key", name="Bob", language="es")
g = Greeter(config)
print(g.greet())  # "Hola, Bob!"
```

## CLI Usage

```bash
# Uses .env automatically — no flags needed for api-key
hello-greet
# Output: Bonjour, Alice!

# Override with flags
hello-greet --name Bob --lang es
# Output: Hola, Bob!

hello-greet --name Bob --loud
# Output: HELLO, BOB!
```

## Project Structure

```
hello-world/
├── pyproject.toml              # Package config (name, version, dependencies)
├── README.md
├── .github/workflows/
│   └── release.yml             # Auto-build wheel on git tag
└── hello_greeter/              # The actual Python package
    ├── __init__.py             # Public API: exports Greeter + GreeterConfig
    ├── config.py               # Reads config from .env / env vars on user's machine
    ├── greeter.py              # Core logic
    └── cli.py                  # CLI entry point (hello-greet command)
```
