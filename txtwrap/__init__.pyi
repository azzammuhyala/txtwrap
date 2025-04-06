# This stub file supports in Python 3.8+

from typing import overload, Callable, Dict, Iterable, List, Literal, Optional, Set, Tuple, Union

# Identities -----------------------------------------------------------------------------------------------------------

__version__: str
__author__: str
__license__: str
__all__: List[str]

# Constants ------------------------------------------------------------------------------------------------------------

LOREM_IPSUM_WORDS: str
LOREM_IPSUM_SENTENCES: str
LOREM_IPSUM_PARAGRAPHS: str

# Wrapper --------------------------------------------------------------------------------------------------------------

class TextWrapper:

    # Dunder / Magic Methods -------------------------------------------------------------------------------------------

    def __init__(
        self,
        width: Union[int, float] = 70,
        line_padding: Union[int, float] = 0,
        method: Literal['mono', 'word'] = 'word',
        alignment: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'] = 'left',
        placeholder: str = '...',
        fillchar: str = ' ',
        separator: Optional[Union[str, Iterable[str]]] = None,
        max_lines: Optional[int] = None,
        preserve_empty: bool = True,
        minimum_width: bool = True,
        justify_last_line: bool = False,
        break_on_hyphens: bool = True,
        sizefunc: Optional[Callable[[str], Union[Tuple[Union[int, float], Union[int, float]], int, float]]] = None
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __copy__(self) -> 'TextWrapper': ...
    def __deepcopy__(self, memo: Dict) -> 'TextWrapper': ...

    # Properties -------------------------------------------------------------------------------------------------------

    @property
    def width(self) -> Union[int, float]: ...
    @property
    def line_padding(self) -> Union[int, float]: ...
    @property
    def method(self) -> Literal['mono', 'word']: ...
    @property
    def alignment(self) -> Literal['left', 'center', 'right', 'fill-left', 'fill-center', 'fill-right']: ...
    @property
    def placeholder(self) -> str: ...
    @property
    def fillchar(self) -> str: ...
    @property
    def separator(self) -> Union[str, Iterable[str], None]: ...
    @property
    def max_lines(self) -> Union[int, None]: ...
    @property
    def preserve_empty(self) -> bool: ...
    @property
    def minimum_width(self) -> bool: ...
    @property
    def justify_last_line(self) -> bool: ...
    @property
    def break_on_hyphens(self) -> bool: ...
    @property
    def sizefunc(self) -> Union[Callable[[str], Union[Tuple[Union[int, float], Union[int, float]],
                                                      int, float]], None]: ...

    # Setters ----------------------------------------------------------------------------------------------------------

    @width.setter
    def width(self, new: Union[int, float]) -> None: ...
    @line_padding.setter
    def line_padding(self, new: Union[int, float]) -> None: ...
    @method.setter
    def method(self, new: Literal['mono', 'word']) -> None: ...
    @alignment.setter
    def alignment(self, new: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center',
                                     'fill-right']) -> None: ...
    @placeholder.setter
    def placeholder(self, new: str) -> None: ...
    @fillchar.setter
    def fillchar(self, new: str) -> None: ...
    @separator.setter
    def separator(self, new: Optional[Union[str, Iterable[str]]]) -> None: ...
    @max_lines.setter
    def max_lines(self, new: Optional[int]) -> None: ...
    @preserve_empty.setter
    def preserve_empty(self, new: bool) -> None: ...
    @minimum_width.setter
    def minimum_width(self, new: bool) -> None: ...
    @justify_last_line.setter
    def justify_last_line(self, new: bool) -> None: ...
    @break_on_hyphens.setter
    def break_on_hyphens(self, new: bool) -> None: ...
    @sizefunc.setter
    def sizefunc(self, new: Optional[Callable[[str], Union[Tuple[Union[int, float], Union[int, float]],
                                                           int, float]]]) -> None: ...

    # Methods ----------------------------------------------------------------------------------------------------------

    def copy(self) -> 'TextWrapper': ...
    def sanitize(self, text: str) -> str: ...
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
    def shorten(self, text: str) -> str: ...

# Interfaces -----------------------------------------------------------------------------------------------------------

def sanitize(
    text: str,
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None
) -> str: ...

@overload
def wrap(
    text: str,
    width: Union[int, float] = 70,
    method: Literal['mono', 'word'] = 'word',
    placeholder: str = '...',
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    break_on_hyphens: bool = True,
    return_details: Literal[False] = False,
    sizefunc: Optional[Callable[[str], Union[int, float]]] = None,
) -> List[str]: ...

@overload
def wrap(
    text: str,
    width: Union[int, float] = 70,
    method: Literal['mono', 'word'] = 'word',
    placeholder: str = '...',
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    break_on_hyphens: bool = True,
    return_details: Literal[True] = True,
    sizefunc: Optional[Callable[[str], Union[int, float]]] = None,
) -> Dict[Literal['wrapped', 'indiced'], Union[List[str], Set[int]]]: ...

@overload
def align(
    text: str,
    width: Union[int, float] = 70,
    line_padding: Union[int, float] = 0,
    method: Literal['mono', 'word'] = 'word',
    alignment: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'] = 'left',
    placeholder: str = '...',
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    minimum_width: bool = True,
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
    alignment: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'] = 'left',
    placeholder: str = '...',
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    minimum_width: bool = True,
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
    alignment: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'] = 'left',
    placeholder: str = '...',
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None,
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    minimum_width: bool = True,
    justify_last_line: bool = False,
    break_on_hyphens: bool = True,
    sizefunc: Optional[Callable[[str], int]] = None
) -> str: ...

def shorten(
    text: str,
    width: Union[int, float] = 70,
    method: Literal['mono', 'word'] = 'word',
    placeholder: str = '...',
    fillchar: str = ' ',
    separator: Optional[Union[str, Iterable[str]]] = None,
    sizefunc: Optional[Callable[[str], Union[int, float]]] = None
) -> str: ...