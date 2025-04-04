"""
A tool for wrapping and filling text.
"""

# Supports only in Python 3.3+

from ._txtwrap import (
    __version__, __author__, __license__,
    LOREM_IPSUM_WORDS, LOREM_IPSUM_SENTENCES, LOREM_IPSUM_PARAGRAPHS,
    TextWrapper,
    sanitize, wrap, align, fillstr, shorten
)

__all__ = [
    'LOREM_IPSUM_WORDS',
    'LOREM_IPSUM_SENTENCES',
    'LOREM_IPSUM_PARAGRAPHS',
    'TextWrapper',
    'sanitize',
    'wrap',
    'align',
    'fillstr',
    'shorten'
]