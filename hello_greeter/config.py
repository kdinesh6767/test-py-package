"""
Configuration — user passes their settings here instead of using .env files.
"""
from dataclasses import dataclass


@dataclass
class GreeterConfig:
    """All user-provided settings live here.

    Example::

        config = GreeterConfig(
            api_key="my-secret-key",
            name="Alice",
            language="es",
        )
    """
    api_key: str = ""
    name: str = "World"
    language: str = "en"
    loud: bool = False
