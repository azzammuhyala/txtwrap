# define the packages

from . import constants as constants
from . import identities as identities
from . import wrapper as wrapper

# define the main variables, functions, classes to be exported

from .constants import (
    LOREM_IPSUM_WORDS as LOREM_IPSUM_WORDS,
    LOREM_IPSUM_SENTENCES as LOREM_IPSUM_SENTENCES,
    LOREM_IPSUM_PARAGRAPHS as LOREM_IPSUM_PARAGRAPHS,
    SEPARATOR_WHITESPACE as SEPARATOR_WHITESPACE,
    SEPARATOR_ESCAPE as SEPARATOR_ESCAPE,
    SEPARATOR_NEWLINE as SEPARATOR_NEWLINE,
    SEPARATOR_NEWLINE_AND_BREAK as SEPARATOR_NEWLINE_AND_BREAK
)

from .identities import (
    __version__ as __version__,
    __author__ as __author__,
    __license__ as __license__
)

from .wrapper import (
    TextWrapper as TextWrapper,
    wrap as wrap,
    align as align,
    fillstr as fillstr,
    shorten as shorten
)