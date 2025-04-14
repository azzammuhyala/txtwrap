"""
A tool for wrapping and filling text.

See txtwrap module documentation on [GitHub](https://github.com/azzammuhyala/txtwrap) or on
[PyPi](https://pypi.org/project/txtwrap) for details.
"""

# Supports only in Python>=3.0.0

from . import constants as constants
from . import identities as identities
from . import wrapper as wrapper

from .identities import __version__, __author__, __license__

from .constants import (
    LOREM_IPSUM_WORDS, LOREM_IPSUM_SENTENCES, LOREM_IPSUM_PARAGRAPHS,
    SEPARATOR_WHITESPACE, SEPARATOR_ESCAPE
)

from .wrapper import (
    TextWrapper,
    sanitize, wrap, align, fillstr, shorten
)

__all__ = [
    'LOREM_IPSUM_WORDS',
    'LOREM_IPSUM_SENTENCES',
    'LOREM_IPSUM_PARAGRAPHS',
    'SEPARATOR_WHITESPACE',
    'SEPARATOR_ESCAPE',
    'TextWrapper',
    'sanitize',
    'wrap',
    'align',
    'fillstr',
    'shorten'
]