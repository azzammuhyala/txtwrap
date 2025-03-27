"""
A tool for wrapping and filling text.
"""

# Supports only in Python 3.3+

from .txtwrap import (
    __version__, __author__, __license__,
    LOREM_IPSUM_WORDS, LOREM_IPSUM_SENTENCES, LOREM_IPSUM_PARAGRAPHS,
    TextWrapper,
    mono, word, wrap, align, fillstr, printwrap, indent, dedent, shorten
)

__all__ = [
    'LOREM_IPSUM_WORDS',
    'LOREM_IPSUM_SENTENCES',
    'LOREM_IPSUM_PARAGRAPHS',
    'TextWrapper',
    'mono',
    'word',
    'wrap',
    'align',
    'fillstr',
    'printwrap',
    'indent',
    'dedent',
    'shorten'
]