"""
Configuration — reads settings from environment variables / .env file
on the machine where the package is installed.

Precedence: explicit argument > environment variable > default value.
"""
import os
from dataclasses import dataclass, field

from dotenv import load_dotenv

load_dotenv()


def _env(key: str, default: str = "") -> str:
    return os.getenv(key, default)


@dataclass
class GreeterConfig:
    """Settings are picked up automatically from env vars / .env file.

    Env vars::

        GREETER_API_KEY   (required)
        GREETER_NAME      (default: "World")
        GREETER_LANGUAGE  (default: "en")
        GREETER_LOUD      (default: "false")

    You can still override any value explicitly::

        config = GreeterConfig(api_key="override-key", name="Alice")
    """
    api_key: str = field(default_factory=lambda: _env("GREETER_API_KEY"))
    name: str = field(default_factory=lambda: _env("GREETER_NAME", "World"))
    language: str = field(default_factory=lambda: _env("GREETER_LANGUAGE", "en"))
    loud: bool = field(default_factory=lambda: _env("GREETER_LOUD", "false").lower() in ("true", "1", "yes"))
