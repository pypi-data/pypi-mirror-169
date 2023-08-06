

class PokeError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, code, message):
        self.message = message
        self.code = code

    def __str__(self):
        return f"Error {self.code}: {self.message}"