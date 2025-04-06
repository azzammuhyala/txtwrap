# TxTWrap🔡
A tool for wrapping and filling text.🔨

- `LOREM_IPSUM_WORDS`
- `LOREM_IPSUM_SENTENCES`
- `LOREM_IPSUM_PARAGRAPHS`
- `TextWrapper` (❇️ Fixed)
- `sanitize`
- `wrap`
- `align`
- `fillstr`
- `shorten`

# Documents📄
This module is inspired by the [`textwrap`](https://docs.python.org/3/library/textwrap.html) module, which provides
several useful functions, along with the [`TextWrapper`](#textwrapper), class that handles all available functions.

The difference between [`txtwrap`](https://pypi.org/project/txtwrap) and
[`textwrap`](https://docs.python.org/3/library/textwrap.html) is that this module is designed not only for wrapping and
filling monospace fonts but also for other font types, such as Arial, Times New Roman, and more.

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

## `TextWrapper`
```py
class TextWrapper:
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
        sizefunc: Optional[Callable[[str], Union[Tuple[Union[int, float], Union[int, float]], int, float]]] = None,
    ) -> None
```
A class that handles all functions available in this module. Each keyword argument corresponds to its attribute.
For example:
```py
wrapper = TextWrapper(width=100)
```
is equivalent to:
```py
wrapper = TextWrapper()
wrapper.width = 100
```
You can reuse [`TextWrapper`](#textwrapper) multiple times or modify its options by assigning new values to its
attributes. However, it is recommended not to reuse [`TextWrapper`](#textwrapper) too frequently inside a specific loop,
as each attribute has type checking, which may reduce performance.

<h1></h1>

### Attributes of [`TextWrapper`](#textwrapper):

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
(Default: `'left'`) The alignment of the wrapped text. Available options: `'left'`, `'center'`, `'right'`,
(`'fill'` or `'fill-left'`), `'fill-center'`, and `'fill-right'`.
- `'left'`: Aligns text to the start of the line.
- `'center'`: Centers text within the line.
- `'right'`: Aligns text to the end of the line.
- `'fill'` or `'fill-left'`: Justifies text across the width but aligns single-word lines or the last line
  (if [`justify_last_line`](#justify_last_line) is `False`) to the left.
- `'fill-center'` and `'fill-right'` work the same way as `'fill-left'`, aligning text according to their respective
  names.

<h1></h1>

#### **`placeholder`**
(Default: `'...'`) The ellipsis used for truncating long lines.

<h1></h1>

#### **`fillchar`**
(Default: `' '`) The character used for padding.

<h1></h1>

#### **`separator`**
(Default: `None`) The character used to separate words.
- `None`: Uses whitespace as the separator.
- `str`: Uses the specified character.
- `Iterable`: Uses multiple specified characters.

<h1></h1>

#### **`max_lines`**
(Default: `None`) The maximum number of wrapped lines.
- `None`: No limit on the number of wrapped lines.
- `int`: Limits the number of wrapped lines to the specified value. (Ensure that [`width`](#width) is not smaller than
         the length of [`placeholder`](#placeholder)).

<h1></h1>

#### **`preserve_empty`**
(Default: `True`) Retains empty lines in the wrapped text.

<h1></h1>

#### **`minimum_width`**
(Default: `True`) Uses the minimum required line width. Some wrapped lines may be shorter than the specified width, so
enabling this attribute removes unnecessary empty space.

<h1></h1>

#### **`justify_last_line`**
(Default: `False`) Determines whether the last line should also be justified
(applies only to `fill-...` alignments).

<h1></h1>

#### **`break_on_hyphens`**
(Default: `True`) Breaks words at hyphens (-). Example `'self-organization'` becomes `'self-'` and `'organization'`.

<h1></h1>

#### **`sizefunc`**
(Default: `None`) A function used to calculate the width and height or only the width of each string.

If the function calculates both width and height, it must return a tuple containing two values:
- The width and height of the string.
- Both values must be of type `int` or `float`.

If the function calculates only the width, it must return a single value of type `int` or `float`.

<h1></h1>

### Methods of [`TextWrapper`](#textwrapper):

<h1></h1>

#### **`copy`**
Creates and returns a copy of the [`TextWrapper`](#textwrapper) object.

<h1></h1>

#### **`sanitize(text)`**
Removes excessive characters from [`separator`](#separator) and replaces them with the [`fillchar`](#fillchar)
character.

For example:
```py
>>> TextWrapper().sanitize("\tHello   World!   ")
'Hello World!'
```

<h1></h1>

#### **`wrap(text, return_details=False)`**
Returns a list of wrapped text strings. If `return_details=True`, returns a dictionary containing:
- `'wrapped'`: A list of wrapped text fragments.
- `'indiced'`: A set of indices marking line breaks (starting from `0`, like programming indices).

For example:
```py
>>> TextWrapper(width=15).wrap(LOREM_IPSUM_WORDS)
['Lorem ipsum', 'odor amet,', 'consectetuer', 'adipiscing', 'elit.']
>>> TextWrapper(width=15).wrap(LOREM_IPSUM_WORDS, return_details=True)
{'wrapped': ['Lorem ipsum', 'odor amet,', 'consectetuer', 'adipiscing', 'elit.'], 'indiced': {4}}
```

<h1></h1>

#### **`align(text, return_details=False)`**
Returns a list of tuples, where each tuple contains `(x, y, text)`, representing the wrapped text along with its
coordinates.
> Note: [`sizefunc`](#sizefunc) must return both width and height.

If `return_details=True`, returns a dictionary containing:
- `'aligned'`: A list of wrapped text with coordinate data.
- `'wrapped'`: The result from wrap.
- `'indiced'`: The indices of line breaks.
- `'size'`: The calculated text size.

For example:
```py
>>> TextWrapper(width=20).align(LOREM_IPSUM_WORDS)
[(0, 0, 'Lorem ipsum odor'), (0, 1, 'amet, consectetuer'), (0, 2, 'adipiscing elit.')]
>>> TextWrapper(width=20).align(LOREM_IPSUM_WORDS, return_details=True)
{'aligned': [(0, 0, 'Lorem ipsum odor'), (0, 1, 'amet, consectetuer'), (0, 2, 'adipiscing elit.')], 'wrapped': [
'Lorem ipsum odor', 'amet, consectetuer', 'adipiscing elit.'], 'indiced': {2}, 'size': (18, 3)}
```

<h1></h1>

#### **`fillstr(text)`**
Returns a string with wrapped text formatted for monospace fonts.
> Note: [`width`](#width), [`line_padding`](#line_padding), and the output of [`sizefunc`](#sizefunc) must return `int`,
not `float`!

For example:
```py
>>> s = TextWrapper(width=20).fillstr(LOREM_IPSUM_WORDS)
>>> s
'Lorem ipsum odor  \namet, consectetuer\nadipiscing elit.  '
>>> print(s)
Lorem ipsum odor  
amet, consectetuer
adipiscing elit.  
```

<h1></h1>

#### **`shorten(text)`**
Returns a truncated string if its length exceeds [`width`](#width), appending [`placeholder`](#placeholder) at the end
if truncated.

For example:
```py
>>> TextWrapper(width=20).shorten(LOREM_IPSUM_WORDS)
'Lorem ipsum odor...'
```

<h1></h1>

# Another examples❓

## Render a wrap text in PyGame🎮
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
    alignment: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'] = 'left',
    placeholder: str = '...',
    max_lines: Optional[int] = None,
    preserve_empty: bool = True,
    minimum_width: bool = True,
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
        minimum_width=minimum_width,
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

width_surface, height_surface = surface.get_size()
pos = ((width - width_surface) / 2, (height - height_surface) / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('#000000')
    screen.blit(surface, pos)
    pygame.display.flip()
    clock.tick(60)
```

## Short a long text🔤
```py
from txtwrap import shorten, LOREM_IPSUM_SENTENCES

print(shorten(LOREM_IPSUM_SENTENCES, width=50, placeholder='…'))
```