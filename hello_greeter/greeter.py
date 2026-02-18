"""
Core logic — config is loaded from env vars / .env on the installed machine.
Explicit arguments to GreeterConfig override env values.
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
    """Greeter that reads config from env vars / .env automatically.

    Example::

        # Set GREETER_API_KEY in .env, then:
        from hello_greeter import Greeter
        g = Greeter()
        print(g.greet())  # "Hello, World!"

        # Or override with explicit config:
        from hello_greeter import Greeter, GreeterConfig
        g = Greeter(GreeterConfig(name="Alice", language="fr"))
        print(g.greet())  # "Bonjour, Alice!"
    """

    def __init__(self, config: GreeterConfig | None = None):
        self.config = config or GreeterConfig()

        if not self.config.api_key:
            raise ValueError(
                "api_key is required. Set GREETER_API_KEY in your .env file "
                "or pass it via GreeterConfig(api_key='...')"
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
