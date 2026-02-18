# hello-greeter

A minimal example of a Python SDK installable via `pip install` from GitHub.

## Installation

```bash
pip install git+https://github.com/<org>/hello-world.git
```

## SDK Usage (in Python code)

```python
from hello_greeter import Greeter, GreeterConfig

# User passes their own config — no .env files needed
config = GreeterConfig(
    api_key="my-secret-key",
    name="Alice",
    language="fr",
)

g = Greeter(config)
print(g.greet())               # "Bonjour, Alice!"
print(g.available_languages()) # ["en", "es", "fr", "de", "ja", "hi", "ta"]
```

## CLI Usage

```bash
hello-greet --api-key my-key --name Alice --lang es
# Output: Hola, Alice!

hello-greet --api-key my-key --name Bob --loud
# Output: HELLO, BOB!
```

## Project Structure

```
hello-world/
├── pyproject.toml              # Package config (name, version, dependencies)
├── README.md
└── hello_greeter/              # The actual Python package
    ├── __init__.py             # Public API: exports Greeter + GreeterConfig
    ├── config.py               # GreeterConfig dataclass (user passes settings here)
    ├── greeter.py              # Core logic (uses config, NOT env vars)
    └── cli.py                  # CLI entry point (hello-greet command)
```
