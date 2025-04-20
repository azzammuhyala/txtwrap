# TxTWrap🔡
A tool for wrapping and filling text.🔨

Package version: **3.1.0** <br>
Python requires version: **>=3.0.0** <br>
Python stub file requires version: **>=3.5.0** <br>

- [`LOREM_IPSUM_WORDS`](#lorem-ipsum)
- [`LOREM_IPSUM_SENTENCES`](#lorem-ipsum)
- [`LOREM_IPSUM_PARAGRAPHS`](#lorem-ipsum)
- [`SEPARATOR_WHITESPACE`](#separators) (✅ Updated)
- [`SEPARATOR_ESCAPE`](#separators) (✅ Updated)
- [`SEPARATOR_NEWLINE`](#separators) (➕ New)
- [`SEPARATOR_NEWLINE_AND_BREAK`](#separators) (➕ New)
- [`TextWrapper`](#textwrapper) (✅ Updated)
- [`wrap`](#wraptext-return_detailsfalse) (✅ Updated)
- [`align`](#aligntext-return_detailsfalse) (✅ Updated)
- [`fillstr`](#fillstrtext) (✅ Updated)
- [`shorten`](#shortentext) (✅ Updated)

# Documents📄
This module is inspired by the [`textwrap`](https://docs.python.org/3/library/textwrap.html) module, which provides
several useful functions, along with the [`TextWrapper`](#textwrapper), class that handles all available functions.

The difference between [`txtwrap`](https://pypi.org/project/txtwrap) and
[`textwrap`](https://docs.python.org/3/library/textwrap.html) is that this module is designed not only for wrapping and
filling _monospace fonts_ but also for other font types, such as _Arial_, _Times New Roman_, and more.

<h1></h1>

## Constants
_File: **txtwrap.constants**_

### Lorem ipsum
```py
LOREM_IPSUM_WORDS
LOREM_IPSUM_SENTENCES
LOREM_IPSUM_PARAGRAPHS
```
A _Lorem Ipsum_ collection of words, sentences, and paragraphs that can be used as examples.
- `LOREM_IPSUM_WORDS` contains a short sentence.
- `LOREM_IPSUM_SENTENCES` contains a slightly longer paragraph.
- `LOREM_IPSUM_PARAGRAPHS` contains several longer paragraphs.

<h1></h1>

### Separators
```py
SEPARATOR_WHITESPACE
SEPARATOR_ESCAPE
SEPARATOR_NEWLINE
SEPARATOR_NEWLINE_AND_BREAK
```
A collection of separators that can be used to separate text.
- `SEPARATOR_WHITESPACE` (for [`word_separator`](#word_separator)) regex contains whitespace characters.
- `SEPARATOR_ESCAPE` (for [`word_separator`](#word_separator)) regex contains whitespace characters including `'\a'`, `'\b'`, and `'\0'`.
- `SEPARATOR_NEWLINE` (for [`newline_separator`](#newline_separator)) regex contains newline characters.
- `SEPARATOR_NEWLINE_AND_BREAK` (for [`newline_separator`](#newline_separator)) regex contains newline characters including breaks tag `<br>`.

<h1></h1>

## `TextWrapper`
_File: **txtwrap.wrapper**_

```py
class TextWrapper:

    def __init__(
        self,
        width: Union[int, float] = 70,
        line_padding: Union[int, float] = 0,
        mode: Literal['mono', 'word'] = 'word',
        alignment: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'] = 'left',
        placeholder: str = '...',
        space_character: str = ' ',
        newline_character: str = '\n',
        word_separator: Optional[Union[str, Tuple[str, int]]] = None,
        newline_separator: Optional[Union[str, Tuple[str, int]]] = None,
        max_lines: Optional[int] = None,
        empty_lines: bool = True,
        minimum_width: bool = True,
        excess_word_separator: bool = False,
        justify_last_line: bool = False,
        break_on_hyphens: bool = True,
        size_function: Optional[Callable[[str], Union[Tuple[Union[int, float], Union[int, float]], int, float]]] = None
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

<h1></h1>

### Attributes of [`TextWrapper`](#textwrapper):

<h1></h1>

#### **`width`**
(Default: `70`) The maximum line length for wrapped text.

<h1></h1>

#### **`line_padding`**
(Default: `0`) The spacing between wrapped lines.

<h1></h1>

#### **`mode`**
(Default: `'word'`) The wrapping mode. Available options:
- `'mono'` make text wraps character by character.
- `'word'` make text wraps word by word.

<h1></h1>

#### **`alignment`**
(Default: `'left'`) The alignment of the wrapped text. Available options:
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

#### **`space_character`**
(Default: `' '`) The character used for padding and for the word separator character.

<h1></h1>

#### **`newline_character`**
(Default: `'\n'`) The character used for line separator.

<h1></h1>

#### **`word_separator`**
(Default: `None`) The character used to separate words.
- `None`: Uses whitespace as the separator.
- `str`: Regex separator in split form.
- `Tuple[str, int]`: Regex separator in split form with flags.

<h1></h1>

#### **`newline_separator`**
(Default: `None`) The character used to separate lines.
- `None`: Uses standard newline as the separator.
- `str`: Regex separator in split form.
- `Tuple[str, int]`: Regex separator in split form with flags.

<h1></h1>

#### **`max_lines`**
(Default: `None`) The maximum number of wrapped lines.
- `None`: No limit on the number of wrapped lines.
- `int`: Limits the number of wrapped lines to the specified value. (Ensure that [`width`](#width) is not smaller than
         the length of [`placeholder`](#placeholder)).

<h1></h1>

#### **`empty_lines`**
(Default: `True`) Retains empty lines in the wrapped text.

<h1></h1>

#### **`minimum_width`**
(Default: `True`) Uses the minimum required line width. Some wrapped lines may be shorter than the specified width, so
enabling this attribute removes unnecessary empty space.

<h1></h1>

#### **`excess_word_separator`**
(Default: `False`) Removes excess separators from between words one at a time.

<h1></h1>

#### **`justify_last_line`**
(Default: `False`) Determines whether the last line should also be justified
(applies only to `fill-...` alignments).

<h1></h1>

#### **`break_on_hyphens`**
(Default: `True`) Breaks words at hyphens (-). Example `'self-organization'` becomes `'self-'` and `'organization'`.

<h1></h1>

#### **`size_function`**
(Default: `None`) A function used to calculate the width and height or only the width of each string.

If the function calculates both width and height, it must return a tuple containing two values:
- The width and height of the string.
- Both values must be of type `int` or `float`.

If the function calculates only the width, it must return a single value of type `int` or `float`.

<h1></h1>

### Methods of [`TextWrapper`](#textwrapper):

> Note: All methods can be called outside the [`TextWrapper`](#textwrapper) like external functions.

For example:
```py
>>> txtwrap.TextWrapper(20, placeholder='[...]').shorten("Hello World!")
```
is equivalent to:
```py
>>> txtwrap.shorten("Hello World!", 20, placeholder='[...]')
```

<h1></h1>

#### **`copy`**
Creates and returns a copy of the [`TextWrapper`](#textwrapper) object. (External function using `copy.copy`)

<h1></h1>

#### **`wrap(text, return_details=False)`**
Returns a list of wrapped text strings. If `return_details=True`, returns a dictionary containing:
- `'wrapped'`: A list of wrapped text fragments.
- `'start_lines'`: A list of indices marking the start of line.
- `'end_lines'`: A list of indices marking the end of line.

For example:
```py
>>> txtwrap.wrap(txtwrap.LOREM_IPSUM_WORDS, width=20)
['Lorem ipsum odor', 'amet, consectetuer', 'adipiscing elit.']
>>> wrapped_info = txtwrap.wrap(txtwrap.LOREM_IPSUM_WORDS, width=20, return_details=True)
>>> start_lines = wrapped_info['start_lines']
>>> end_lines = wrapped_info['end_lines']
>>> wrapped_info
{'wrapped': ['Lorem ipsum odor', 'amet, consectetuer', 'adipiscing elit.'], 'start_lines': [1], 'end_lines': [3]}
>>> wrapped_info['wrapped'][start_lines[0] - 1]
'Lorem ipsum odor'
>>> wrapped_info['wrapped'][end_lines[0] - 1]
'adipiscing elit.'
```

<h1></h1>

#### **`align(text, return_details=False)`**
Returns a list of tuples, where each tuple contains `(xPosition, yPosition, text)`, representing the wrapped text along
with its coordinates.
> Note: [`size_function`](#size_function) must return both width and height.

If `return_details=True`, returns a dictionary containing:
- `'aligned'`: A list of wrapped text with coordinate data.
- `'wrapped'`: A list of wrapped text fragments.
- `'start_lines'`: A list of indices marking the start of line.
- `'end_lines'`: A list of indices marking the end of line.
- `'size'`: A calculated text size.

For example:
```py
>>> txtwrap.align(txtwrap.LOREM_IPSUM_WORDS, width=20)
[(0, 0, 'Lorem ipsum odor'), (0, 1, 'amet, consectetuer'), (0, 2, 'adipiscing elit.')]
>>> aligned_info = txtwrap.align(txtwrap.LOREM_IPSUM_WORDS, width=20, return_details=True)
>>> start_lines = aligned_info['start_lines']
>>> end_lines = aligned_info['end_lines']
>>> aligned_info
{'aligned': [(0, 0, 'Lorem ipsum odor'), (0, 1, 'amet, consectetuer'), (0, 2, 'adipiscing elit.')], 'wrapped': [
'Lorem ipsum odor', 'amet, consectetuer', 'adipiscing elit.'], 'start_lines': [1], 'end_lines': [3], 'size': (18, 3)}
>>> aligned_info['wrapped'][start_lines[0] - 1]
'Lorem ipsum odor'
>>> aligned_info['wrapped'][end_lines[0] - 1]
'adipiscing elit.'
```

<h1></h1>

#### **`fillstr(text)`**
Returns a string with wrapped text formatted for monospace fonts.
> Note: [`width`](#width), [`line_padding`](#line_padding), and the output of [`size_function`](#size_function)
(size or just length) must return `int`, not `float`!

For example:
```py
>>> s = txtwrap.fillstr(txtwrap.LOREM_IPSUM_WORDS, width=20)
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
>>> txtwrap.shorten(txtwrap.LOREM_IPSUM_WORDS, width=20)
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
    wrap_mode: Literal['word', 'mono'] = 'word',
    alignment: Literal['left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'] = 'left',
    placeholder: str = '...',
    max_lines: Optional[int] = None,
    empty_lines: bool = True,
    minimum_width: bool = True,
    excess_word_separator: bool = False,
    justify_last_line: bool = False,
    break_on_hyphens: bool = True

) -> pygame.Surface:

    align_info = align(
        text=text,
        width=width,
        line_padding=line_padding,
        mode=wrap_mode,
        alignment=alignment,
        placeholder=placeholder,
        max_lines=max_lines,
        empty_lines=empty_lines,
        minimum_width=minimum_width,
        excess_word_separator=excess_word_separator,
        justify_last_line=justify_last_line,
        break_on_hyphens=break_on_hyphens,
        return_details=True,
        size_function=font.size
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

print(shorten(LOREM_IPSUM_SENTENCES, width=50, placeholder='\u2026'))
```