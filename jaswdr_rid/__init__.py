__version__ = "1.0.3"

from .exceptions import InvalidResourceError, NotResourceError
from .resource import Resource

__all__ = ["Resource", "InvalidResourceError", "NotResourceError"]
