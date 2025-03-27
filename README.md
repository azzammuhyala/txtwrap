# TxTWrap🔡
A tool for wrapping and filling text.🔨

## All constants, functions, and classes❕
- `LOREM_IPSUM_WORDS`
- `LOREM_IPSUM_SENTENCES`
- `LOREM_IPSUM_PARAGRAPHS`
- `TextWrapper` (Updated)
- `mono` (Updated)
- `word` (Updated)
- `wrap` (Updated)
- `align` (Updated)
- `fillstr` (Updated)
- `printwrap` (Updated)
- `indent` (Updated)
- `dedent` (Updated)
- `shorten` (Updated)

## Documents📄
This module is inspired by the [`textwrap`](https://docs.python.org/3/library/textwrap.html) module,
which provides several useful functions, along with the [`TextWrapper`](#textwrapper), class that
handles all available functions.

The difference between [`txtwrap`](https://pypi.org/project/txtwrap) and
[`textwrap`](https://docs.python.org/3/library/textwrap.html) is that this module is designed not
only for wrapping and filling monospace fonts but also for other font types, such as Arial,
Times New Roman, and more. Additionally, this module offers extra functions that are not available
in the original [`textwrap`](https://docs.python.org/3/library/textwrap.html).

<!-- tag <h1> boundary line -->
<h1></h1>

```py
LOREM_IPSUM_WORDS
LOREM_IPSUM_SENTENCES
LOREM_IPSUM_PARAGRAPHS
```
A collection of words, sentences, and paragraphs that can be used as examples.
- `LOREM_IPSUM_WORDS` contains a short Lorem Ipsum sentence.
- `LOREM_IPSUM_SENTENCES` contains a slightly longer paragraph.
- `LOREM_IPSUM_PARAGRAPHS` contains several longer paragraphs.

<h1></h1>

### `TextWrapper`
```py
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

    ) -> None
```

A class that handles all functions available in this module. Each keyword argument corresponds to
its attribute. For example:
```py
wrapper = TextWrapper(width=100)
```
is equivalent to:
```py
wrapper = TextWrapper()
wrapper.width = 100
```
You can reuse [`TextWrapper`](#textwrapper) multiple times or modify its options by assigning new
values to its attributes. However, it is recommended not to reuse [`TextWrapper`](#textwrapper) too
frequently inside a specific loop, as each attribute has type checking, which may reduce
performance.

<h1></h1>

**Attributes of [`TextWrapper`](#textwrapper):**

<h1></h1>

#### **`width`**
(Default: `70`) The maximum line length for wrapped text.

<h1></h1>

#### **`line_padding`**
(Default: `0`) The spacing between wrapped lines.

<h1></h1>

#### **`method`**
(Default: `'word'`) The wrapping method. Available options: `'mono'` and `'word'`.
- `'mono'` method wraps text character by character.
- `'word'` method wraps text word by word.

<h1></h1>

#### **`alignment`**
(Default: `'left'`) The alignment of the wrapped text. Available options: `'left'`, `'center'`,
`'right'`, (`'fill'` or `'fill-left'`), `'fill-center'`, and `'fill-right'`.
- `'left'`: Aligns text to the start of the line.
- `'center'`: Centers text within the line.
- `'right'`: Aligns text to the end of the line.
- `'fill'` or `'fill-left'`: Justifies text across the width but aligns single-word lines or the
  last line (if [`justify_last_line`](#justify_last_line) is `False`) to the left.
- `'fill-center'` and `'fill-right'` work the same way as `'fill-left'`, aligning text according to
  their respective names.

<h1></h1>

#### **`fillchar`**
(Default: `' '`) The character used for padding.

<h1></h1>

#### **`placeholder`**
(Default: `'...'`) The ellipsis used for truncating long lines.

<h1></h1>

#### **`prefix`**
(Default: `None`) The prefix used for the [`indent`](#indenttext) or [`dedent`](#dedenttext)
methods.
- [`indent`](#indenttext) method adds a prefix to the beginning of each line
  (must be of type `str`).
- [`dedent`](#dedenttext) method removes the prefix from each line:
    - `None` removes leading whitespace.
    - `str` removes the specified character.
    - `Iterable` (e.g., `set`, `list`, `tuple`, etc.) removes multiple specified characters, where
                 each must be a single-character `str`.

<h1></h1>

#### **`separator`**
(Default: `None`) The character used to separate words.
- `None`: Uses whitespace as the separator.
- `str`: Uses the specified character.
- `Iterable`: Uses multiple specified characters, where each must be a single-character `str`.

<h1></h1>

#### **`max_lines`**
(Default: `None`) The maximum number of wrapped lines.
- `None`: No limit on the number of wrapped lines.
- `int`: Limits the number of wrapped lines to the specified value. (Ensure that [`width`](#width)
         is not smaller than the length of [`placeholder`](#placeholder)).

<h1></h1>

#### **`preserve_empty`**
(Default: `True`) Retains empty lines in the wrapped text.

<h1></h1>

#### **`use_minimum_width`**
(Default: `True`) Uses the minimum required line width. Some wrapped lines may be shorter than the
specified width, so enabling this attribute removes unnecessary empty space.

<h1></h1>

#### **`justify_last_line`**
(Default: `False`) Determines whether the last line should also be justified
(applies only to `fill-...` alignments).

<h1></h1>

#### **`break_on_hyphens`**
(Default: `True`) Breaks words at hyphens (-).
Example: `'self-organization'` becomes `['self-', 'organization']`.

<h1></h1>

#### **`sizefunc`**
(Default: `None`) A function used to calculate the width and height of each string. The function
must return a tuple containing two values:
- The width and height of the string.
- Both values must be of type int or float.

<h1></h1>

#### **`predicate`**
(Default: `None`) A function used by the [`indent`](#indenttext) or [`dedent`](#dedenttext) methods
to filter which lines should have a prefix added or removed.

<h1></h1>

**Methods of [`TextWrapper`](#textwrapper):**

<h1></h1>

#### **`copy`**
Creates and returns a copy of the [`TextWrapper`](#textwrapper) object.

<h1></h1>

#### **`mono(text)`**
Returns a list of strings, where the text is wrapped per character.
> Note: Does not support newline characters.

For example:
```py
>>> TextWrapper(width=5).mono("Don't Touch My\nPizza!")
["Don't", ' Touc', 'h My ', 'Pizza', '!']
```

<h1></h1>

#### **`word(text)`**
Returns a list of strings, where the text is wrapped per word.
> Note: Does not support newline characters.

For example:
```py
>>> TextWrapper(width=5).word("Don't Touch My\nJelly!")
["Don't", 'Touch', 'My', 'Jelly', '!']
```

<h1></h1>

#### **`wrap(text, return_details=False)`**
Returns a list of wrapped text strings. If `return_details=True`, returns a dictionary containing:
- `'wrapped'`: A list of wrapped text fragments.
- `'indiced'`: A set of indices marking line breaks (starting from `0`, like programming indices).
> Note: Supports newline characters.

For example:
```py
>>> TextWrapper(width=15).wrap("I don't like blue cheese\ncuz it is realy smelly!")
["I don't like", 'blue cheese', 'cuz it is realy', 'smelly!']
>>> TextWrapper(width=15).wrap("You touch my pizza your gonna to die!", return_details=True)
{'wrapped': ['You touch my', 'pizza your', 'gonna to die!'], 'indiced': {2}}
```

<h1></h1>

#### **`align(text, return_details=False)`**
Returns a list of tuples, where each tuple contains `(x, y, text)`, representing the wrapped text
along with its coordinates. If `return_details=True`, returns a dictionary containing:
- `'aligned'`: A list of wrapped text with coordinate data.
- `'wrapped'`: The result from wrap.
- `'indiced'`: The indices of line breaks.
- `'size'`: The calculated text size.

For example:
```py
>>> TextWrapper(width=20).align("Bang beli bawang, beli bawang gk pakek kulit")
[(0, 0, 'Bang beli bawang,'), (0, 1, 'beli bawang gk pakek'), (0, 2, 'kulit')]
>>> TextWrapper(width=20).align("Bang bawang gk pakek kulit..", return_details=True)
{'aligned': [(0, 0, 'Bang bawang gk pakek'), (0, 1, 'kulit..')], 'wrapped': ['Bang bawang gk pakek',
'kulit..'], 'indiced': {1}, 'size': (20, 2)}
```

<h1></h1>

#### **`fillstr(text)`**
Returns a string with wrapped text formatted for monospace fonts.
> Note: [`width`](#width), [`line_padding`](#line_padding), and the output of
[`sizefunc`](#sizefunc) must return `int`, not `float`!

For example:
```py
>>> s = TextWrapper(width=20).fillstr("Tung tung tung tung tung tung sahur")
>>> s
'Tung tung tung tung\ntung tung sahur    '
>>> print(s)
Tung tung tung tung
tung tung sahur
```

<h1></h1>

#### **`indent(text)`**
Returns a string where each line is prefixed with [`prefix`](#prefix).

For example:
```py
>>> s = TextWrapper(prefix='> ').indent("Hello\nWorld!")
'> Hello\n> World!'
>>> print(s)
> Hello
> World!
```

<h1></h1>

#### **`dedent(text)`**
Returns a string where [`prefix`](#prefix) is removed from the start of each line.

For example:
```py
>>> s = TextWrapper(prefix='>>> ').dedent(">>> Hello\n>>> World!")
>>> s
'Hello\nWorld!'
>>> print(s)
Hello
World!
```

<h1></h1>

#### **`shorten(text)`**
Returns a truncated string if its length exceeds [`width`](#width), appending 
[`placeholder`](#placeholder) at the end if truncated.

For example:
```py
>>> TextWrapper(width=20).shorten("This is a very long string that will be shortened")
'This is a very lo...'
```

<h1></h1>

**External Functions:**

<h1></h1>

### `printwrap`
```py
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
) -> None
```

[`printwrap`](#printwrap) is a function similar to Python's built-in `print`, but it includes text
wrapping functionality. It utilizes the [`fillstr`](#fillstrtext) method.

#### `*values`
Arguments to be printed.

#### `sep`
Separator between values.
> Note: This does not refer to the [`separator`](#separator) attribute in
[`TextWrapper`](#textwrapper) or [`fillstr`](#fillstrtext).

#### `end`
End character(s) between printed values.

#### `wrap`
An instance of [`TextWrapper`](#textwrapper). If set to `None`, a new [`TextWrapper`](#textwrapper)
object is created on each call.

#### `file`
The standard `file` argument for Python's `print` function.

#### `flush`
The standard `flush` argument for Python's `print` function.

#### `size`
Defines the width and height of the [`TextWrapper`](#textwrapper).
- If set to a `tuple`, it specifies the width and height manually. The height can be None, meaning
  no maximum height limit (taken from max_lines).
- If set to `'auto'` when using a [`TextWrapper`](#textwrapper) instance in wrap, it automatically
  adjusts the following attributes:
    - [`width`](#width)
    - [`line_padding`](#line_padding) (set to `0`)
    - [`max_lines`](#max_lines)

#### `default_size`
The default width and height for wrapping, used when:
- `os.get_terminal_size()` fails to retrieve terminal dimensions.
- The [`size`](#size) parameter is invalid.

#### `apply_height`
Determines whether the wrapper should enforce a height limit, even if a height is defined.

#### `use_minimum_width, **kwargs`
Additional arguments passed to external methods of [`fillstr`](#fillstrtext).

<h1></h1>

## Another examples❓

### Render a wrap text in PyGame🎮
```py
from typing import Literal, Optional
from txtwrap import align, LOREM_IPSUM_PARAGRAPHS
import pygame

def render_wrap(

    font: pygame.Font,
    text: str,
    width: int,
    antialias: bool,
    color: pygame.Color,
    background: Optional[pygame.Color] = None,
    line_padding: int = 0,
    method: Literal['word', 'mono'] = 'word',
    alignment: Literal['left', 'center', 'right', 'fill',
                       'fill-left', 'fill-center', 'fill-right'] = 'left',
    placeholder: str = '...',
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    use_minimum_width: bool = True,
    justify_last_line: bool = False,
    break_on_hyphens: bool = True

) -> pygame.Surface:

    align_info = align(
        text=text,
        width=width,
        line_padding=line_padding,
        method=method,
        alignment=alignment,
        placeholder=placeholder,
        max_lines=max_lines,
        preserve_empty=preserve_empty,
        use_minimum_width=use_minimum_width,
        justify_last_line=justify_last_line,
        break_on_hyphens=break_on_hyphens,
        return_details=True,
        sizefunc=font.size
    )

    surface = pygame.Surface(align_info['size'], pygame.SRCALPHA)

    if background is not None:
        surface.fill(background)

    for x, y, text in align_info['aligned']:
        surface.blit(font.render(text, antialias, color), (x, y))

    return surface

# Example usage:
pygame.init()
pygame.display.set_caption("Lorem Ipsum")

running = True
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

surface = render_wrap(
    font=pygame.font.SysFont('Arial', 18),
    text=LOREM_IPSUM_PARAGRAPHS,
    width=width,
    antialias=True,
    color='#ffffff',
    background='#303030',
    alignment='fill'
)

wsurf, hsurf = surface.get_size()
pos = ((width - wsurf) / 2, (height - hsurf) / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('#000000')
    screen.blit(surface, pos)
    pygame.display.flip()
    clock.tick(60)
```

### Print a wrap text to terminal🔡
```py
from txtwrap import printwrap, LOREM_IPSUM_WORDS

width = 20

printwrap(LOREM_IPSUM_WORDS, size=(width, None), alignment='left')
print('=' * width)
printwrap(LOREM_IPSUM_WORDS, size=(width, None), alignment='center')
print('=' * width)
printwrap(LOREM_IPSUM_WORDS, size=(width, None), alignment='right')
print('=' * width)
printwrap(LOREM_IPSUM_WORDS, size=(width, None), alignment='fill') # or alignment='fill-left'
print('=' * width)
printwrap(LOREM_IPSUM_WORDS, size=(width, None), alignment='fill-center')
print('=' * width)
printwrap(LOREM_IPSUM_WORDS, size=(width, None), alignment='fill-right')
```

### Short a long text🔤
```py
from txtwrap import shorten, LOREM_IPSUM_SENTENCES

print(shorten(LOREM_IPSUM_SENTENCES, width=20, placeholder='…'))
```

### Bonus🎁 - Print a colorfull text to terminal🔥
```py
# Run this code in a terminal that supports ansi characters

from re import compile
from random import randint
from txtwrap import printwrap, LOREM_IPSUM_PARAGRAPHS

# Set the text to be printed here
text = LOREM_IPSUM_PARAGRAPHS

remove_ansi_re = compile(r'\x1b\[(K|.*?m)').sub

def len_no_ansi(s: str):
    return len(remove_ansi_re('', s))

while True:
    printwrap(
        ''.join('\x1b[{}m{}'.format(randint(31, 36), char) for char in text),
        end='\x1b[0m\x1b[H\x1b[J',
        alignment='fill',
        lenfunc=len_no_ansi
    )
```