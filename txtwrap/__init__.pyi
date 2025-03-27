# This stub files supports in Python 3.9+, I guess..

from typing import (
    overload, Callable, Dict, IO, Iterable, List, Literal, Optional, Set, Tuple, Union
)

# Identities ---------------------------------------------------------------------------------------

__version__: str
__author__: str
__license__: str
__all__: List[str]

# Constants ----------------------------------------------------------------------------------------

LOREM_IPSUM_WORDS: str
LOREM_IPSUM_SENTENCES: str
LOREM_IPSUM_PARAGRAPHS: str

# Wrapper ------------------------------------------------------------------------------------------

class TextWrapper:

    def __init__(

        self,
        width: Union[int, float] = 70,
        line_padding: Union[int, float] = 0,
        method: Literal['mono', 'word'] = 'word',
        alignment: Literal['left', 'center', 'right', 'fill',
                           'fill-left', 'fill-center', 'fill-right'] = 'left',
        fillchar: str = ' ',
        placeholder: str = '...',
        prefix: Optional[Union[str, Iterable[str]]] = None,
        separator: Optional[Union[str, Iterable[str]]] = None,
        max_lines: Optional[int] = None,
        preserve_empty: bool = True,
        use_minimum_width: bool = True,
        justify_last_line: bool = False,
        break_on_hyphens: bool = True,
        sizefunc: Optional[Callable[[str], Tuple[Union[int, float], Union[int, float]]]] = None,
        predicate: Optional[Callable[[str], bool]] = None

    ) -> None: ...

    def __repr__(self) -> str: ...
    def __copy__(self) -> 'TextWrapper': ...
    def __deepcopy__(self, memo: Dict) -> 'TextWrapper': ...

    # Properties -----------------------------------------------------------------------------------

    @property
    def width(self) -> Union[int, float]: ...
    @property
    def line_padding(self) -> Union[int, float]: ...
    @property
    def method(self) -> Literal['mono', 'word']: ...
    @property
    def alignment(self) -> Literal['left', 'center', 'right', 'fill',
                                   'fill-left', 'fill-center', 'fill-right']: ...
    @property
    def fillchar(self) -> str: ...
    @property
    def placeholder(self) -> str: ...
    @property
    def prefix(self) -> Union[str, Iterable[str], None]: ...
    @property
    def separator(self) -> Union[str, Iterable[str], None]: ...
    @property
    def max_lines(self) -> Union[int, None]: ...
    @property
    def preserve_empty(self) -> bool: ...
    @property
    def use_minimum_width(self) -> bool: ...
    @property
    def justify_last_line(self) -> bool: ...
    @property
    def break_on_hyphens(self) -> bool: ...
    @property
    def sizefunc(self) -> Union[Callable[[str], Tuple[Union[int, float],
                                                      Union[int, float]]], None]: ...
    @property
    def predicate(self) -> Union[Callable[[str], bool], None]: ...

    # Setters --------------------------------------------------------------------------------------

    @width.setter
    def width(self, new: Union[int, float]) -> None: ...
    @line_padding.setter
    def line_padding(self, new: Union[int, float]) -> None: ...
    @method.setter
    def method(self, new: Literal['mono', 'word']) -> None: ...
    @alignment.setter
    def alignment(self, new: Literal['left', 'center', 'right', 'fill',
                                     'fill-left', 'fill-center', 'fill-right']) -> None: ...
    @fillchar.setter
    def fillchar(self, new: str) -> None: ...
    @placeholder.setter
    def placeholder(self, new: str) -> None: ...
    @prefix.setter
    def prefix(self, new: Optional[Union[str, Iterable[str]]]) -> None: ...
    @separator.setter
    def separator(self, new: Optional[Union[str, Iterable[str]]]) -> None: ...
    @max_lines.setter
    def max_lines(self, new: Optional[int]) -> None: ...
    @preserve_empty.setter
    def preserve_empty(self, new: bool) -> None: ...
    @use_minimum_width.setter
    def use_minimum_width(self, new: bool) -> None: ...
    @justify_last_line.setter
    def justify_last_line(self, new: bool) -> None: ...
    @break_on_hyphens.setter
    def break_on_hyphens(self, new: bool) -> None: ...
    @sizefunc.setter
    def sizefunc(self, new: Optional[Callable[[str], Tuple[Union[int, float],
                                                  Union[int, float]]]]) -> None: ...
    @predicate.setter
    def predicate(self, new: Optional[Callable[[str], bool]]) -> None: ...

    # Methods --------------------------------------------------------------------------------------

    def copy(self) -> 'TextWrapper': ...
    def mono(self, text: str) -> List[str]: ...
    def word(self, text: str) -> List[str]: ...
    @overload
    def wrap(
        self,
        text: str,
        return_details: Literal[False] = False
    ) -> List[str]: ...
    @overload
    def wrap(
        self,
        text: str,
        return_details: Literal[True] = True
    ) -> Dict[Literal['wrapped', 'indiced'], Union[List[str], Set[int]]]: ...
    @overload
    def align(
        self,
        text: str,
        return_details: Literal[False] = False
    ) -> List[Tuple[Union[int, float], Union[int, float], str]]: ...
    @overload
    def align(
        self,
        text: str,
        return_details: Literal[True] = True
    ) -> Dict[Literal['aligned', 'wrapped', 'indiced',  'size'],
              Union[List[Tuple[Union[int, float], Union[int, float], str]],
                    List[str],
                    Set[int],
                    Tuple[Union[int, float], Union[int, float]]]]: ...
    def fillstr(self, text: str) -> str: ...
    def indent(self, text: str) -> str: ...
    def dedent(self, text: str) -> str: ...
    def shorten(self, text: str) -> str: ...

# Interfaces ---------------------------------------------------------------------------------------

def mono(
    text: str,
    width: Union[int, float] = 70,
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    lenfunc: Optional[Callable[[str], Union[int, float]]] = None
) -> List[str]: ...

def word(
    text: str,
    width: Union[int, float] = 70,
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    break_on_hyphens: bool = True,
    lenfunc: Optional[Callable[[str], Union[int, float]]] = None,
) -> List[str]: ...

@overload
def wrap(
    text: str,
    width: Union[int, float] = 70,
    method: Literal['mono', 'word'] = 'word',
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    break_on_hyphens: bool = True,
    return_details: Literal[False] = False,
    lenfunc: Optional[Callable[[str], Union[int, float]]] = None,
) -> List[str]: ...

@overload
def wrap(
    text: str,
    width: Union[int, float] = 70,
    method: Literal['mono', 'word'] = 'word',
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    break_on_hyphens: bool = True,
    return_details: Literal[True] = True,
    lenfunc: Optional[Callable[[str], Union[int, float]]] = None,
) -> Dict[Literal['wrapped', 'indiced'], Union[List[str], Set[int]]]: ...

@overload
def align(
    text: str,
    width: Union[int, float] = 70,
    line_padding: Union[int, float] = 0,
    method: Literal['mono', 'word'] = 'word',
    alignment: Literal['left', 'center', 'right', 'fill',
                       'fill-left', 'fill-center', 'fill-right'] = 'left',
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    use_minimum_width: bool = True,
    justify_last_line: bool = False,
    break_on_hyphens: bool = True,
    return_details: Literal[False] = False,
    sizefunc: Optional[Callable[[str], Tuple[Union[int, float], Union[int, float]]]] = None
) -> List[Tuple[Union[int, float], Union[int, float], str]]: ...

@overload
def align(
    text: str,
    width: Union[int, float] = 70,
    line_padding: Union[int, float] = 0,
    method: Literal['mono', 'word'] = 'word',
    alignment: Literal['left', 'center', 'right', 'fill',
                       'fill-left', 'fill-center', 'fill-right'] = 'left',
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    use_minimum_width: bool = True,
    justify_last_line: bool = False,
    break_on_hyphens: bool = True,
    return_details: Literal[True] = True,
    sizefunc: Optional[Callable[[str], Tuple[Union[int, float], Union[int, float]]]] = None
) -> Dict[Literal['aligned', 'wrapped', 'indiced', 'size'],
          Union[List[Tuple[Union[int, float], Union[int, float], str]],
                List[str],
                Set[int],
                Tuple[Union[int, float], Union[int, float]]]]: ...

def fillstr(
    text: str,
    width: int = 70,
    line_padding: int = 0,
    method: Literal['mono', 'word'] = 'word',
    alignment: Literal['left', 'center', 'right', 'fill',
                       'fill-left', 'fill-center', 'fill-right'] = 'left',
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    use_minimum_width: bool = True,
    justify_last_line: bool = False,
    break_on_hyphens: bool = True,
    lenfunc: Optional[Callable[[str], int]] = None
) -> str: ...

def printwrap(
    *values: object,
    sep: Optional[str] = ' ',
    end: Optional[str] = '\n',
    wrap: Optional[TextWrapper] = None,
    file: Optional[IO] = None,
    flush: bool = False,
    size: Optional[Union[Tuple[int, Optional[int]], Literal['auto']]] = None,
    default_size: Tuple[int, Optional[int]] = (70, None),
    apply_height: bool = True,
    use_minimum_width: bool = False,
    **kwargs
) -> None: ...

def indent(
    text: str,
    prefix: str,
    predicate: Optional[Callable[[str], bool]] = None,
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None
) -> str: ...

def dedent(
    text: str,
    prefix: Optional[Union[str, Iterable[str]]] = None,
    predicate: Optional[Callable[[str], bool]] = None,
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None
) -> str: ...

def shorten(
    text: str,
    width: Union[int, float] = 70,
    method: Literal['mono', 'word'] = 'word',
    fillchar: str = ' ',
    placeholder: str = '...',
    separator: Optional[Union[str, Iterable[str]]] = None,
    lenfunc: Optional[Callable[[str], Union[int, float]]] = None
) -> str: ...