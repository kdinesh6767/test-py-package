"""
Core logic — this is where the actual work happens.
The user's config (api_key, name, language) is passed in, NOT read from env.
"""
from .config import GreeterConfig

TRANSLATIONS = {
    "en": "Hello",
    "es": "Hola",
    "fr": "Bonjour",
    "de": "Hallo",
    "ja": "Konnichiwa",
    "hi": "Namaste",
    "ta": "Vanakkam",
}


class Greeter:
    """Simple greeter that uses user-provided config.

    Example::

        from hello_greeter import Greeter, GreeterConfig

        config = GreeterConfig(api_key="my-key", name="Alice", language="fr")
        g = Greeter(config)
        print(g.greet())       # "Bonjour, Alice!"
        print(g.get_api_key()) # "my-key"
    """

    def __init__(self, config: GreeterConfig | None = None):
        self.config = config or GreeterConfig()

        if not self.config.api_key:
            raise ValueError(
                "api_key is required. Pass it via GreeterConfig(api_key='...')"
            )

    def greet(self) -> str:
        word = TRANSLATIONS.get(self.config.language, "Hello")
        message = f"{word}, {self.config.name}!"
        if self.config.loud:
            message = message.upper()
        return message

    def available_languages(self) -> list[str]:
        return list(TRANSLATIONS.keys())

    def get_api_key(self) -> str:
        masked = self.config.api_key[:4] + "****"
        return masked
