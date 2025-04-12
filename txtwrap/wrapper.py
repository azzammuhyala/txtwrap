"""
Internal txtwrap module
"""

from collections.abc import Iterable
from re import compile, escape

# Tools ----------------------------------------------------------------------------------------------------------------

pdict = type('pdict', (dict,), {
    '__repr__': lambda self : '{}({})'.format(self.__class__.__name__, dict.__repr__(self)),
    '__setattr__': dict.__setitem__,
    '__getattr__': lambda self, key: self.get(key, None),
    '__delattr__': dict.__delitem__
})

split_hyphenated = compile(r'(?<=-)(?=(?!-).)').split

def mono(text, width, _0, _1, lenfunc, sanitize, _2):
    wrapped = []
    current_char = ''

    for char in sanitize(text):
        if lenfunc(current_char + char) <= width:
            current_char += char
        else:
            wrapped.append(current_char)
            current_char = char

    if current_char:
        wrapped.append(current_char)

    return wrapped

def word(text, width, fillchar, break_on_hyphens, lenfunc, sanitize, split_separator):
    wrapped = []
    current_line = ''

    for word in split_separator(text):
        test_line = current_line + fillchar + word if current_line else word

        if lenfunc(test_line) <= width:
            current_line = test_line
        else:
            if current_line:
                wrapped.append(current_line)

            current_line = ''

            if break_on_hyphens:
                for part in split_hyphenated(word):
                    for wrapped_part in mono(part, width, None, None, lenfunc, sanitize, None):
                        if lenfunc(current_line + wrapped_part) <= width:
                            current_line += wrapped_part
                        else:
                            if current_line:
                                wrapped.append(current_line)
                            current_line = wrapped_part
            else:
                for part in mono(word, width, None, None, lenfunc, sanitize, None):
                    if lenfunc(current_line + part) <= width:
                        current_line += part
                    else:
                        if current_line:
                            wrapped.append(current_line)
                        current_line = part

    if current_line:
        wrapped.append(current_line)

    return wrapped

def jusitfy_align_left(aligned_positions, text, _0, _1, offset_y):
    aligned_positions.append((0, offset_y, text))

def justify_align_center(aligned_positions, text, width, text_width, offset_y):
    aligned_positions.append(((width - text_width) / 2, offset_y, text))

def justify_align_right(aligned_positions, text, width, text_width, offset_y):
    aligned_positions.append((width - text_width, offset_y, text))

def justify_fillstr_left(justified_lines, text, width, text_width, fillchar):
    justified_lines.append(text + fillchar * (width - text_width))

def justify_fillstr_center(justified_lines, text, width, text_width, fillchar):
    extra_space = width - text_width
    left_space = extra_space // 2
    justified_lines.append(fillchar * left_space + text + fillchar * (extra_space - left_space))

def justify_fillstr_right(justified_lines, text, width, text_width, fillchar):
    justified_lines.append(fillchar * (width - text_width) + text)

# Identities -----------------------------------------------------------------------------------------------------------

__version__ = '2.3.2'
__author__ = 'azzammuhyala'
__license__ = 'MIT'

# Constants ------------------------------------------------------------------------------------------------------------

LOREM_IPSUM_WORDS = 'Lorem ipsum odor amet, consectetuer adipiscing elit.'
LOREM_IPSUM_SENTENCES = (
    'Lorem ipsum odor amet, consectetuer adipiscing elit. In malesuada eros natoque urna felis diam aptent donec. Cubil'
    'ia libero morbi fusce tempus, luctus aenean augue. Mus senectus rutrum phasellus fusce dictum platea. Eros a integ'
    'er nec fusce erat urna.'
)
LOREM_IPSUM_PARAGRAPHS = (
    'Lorem ipsum odor amet, consectetuer adipiscing elit. Nulla porta ex condimentum velit facilisi; consequat congue. '
    'Tristique duis sociosqu aliquam semper sit id. Nisi morbi purus, nascetur elit pellentesque venenatis. Velit commo'
    'do molestie potenti placerat faucibus convallis. Himenaeos dapibus ipsum natoque nam dapibus habitasse diam. Viver'
    'ra ac porttitor cras tempor cras. Pharetra habitant nibh dui ipsum scelerisque cras? Efficitur phasellus etiam con'
    'gue taciti tortor quam. Volutpat quam vulputate condimentum hendrerit justo congue iaculis nisl nullam.\n\nIncepto'
    's tempus nostra fringilla arcu; tellus blandit facilisi risus. Platea bibendum tristique lectus nunc placerat id a'
    'liquam. Eu arcu nisl mattis potenti elementum. Dignissim vivamus montes volutpat litora felis fusce ultrices. Vulp'
    'utate magna nascetur bibendum inceptos scelerisque morbi posuere. Consequat dolor netus augue augue tristique cura'
    'bitur habitasse bibendum. Consectetur est per eros semper, magnis interdum libero. Arcu adipiscing litora metus fr'
    'ingilla varius gravida congue tellus adipiscing. Blandit nulla mauris nullam ante metus curae scelerisque.\n\nSem '
    'varius sodales ut volutpat imperdiet turpis primis nullam. At gravida tincidunt phasellus lacus duis integer eros '
    'penatibus. Interdum mauris molestie posuere nascetur dignissim himenaeos; magna et quisque. Dignissim malesuada et'
    'iam donec vehicula aliquet bibendum. Magna dapibus sapien semper parturient id dis? Pretium orci ante leo, porta t'
    'incidunt molestie. Malesuada dictumst commodo consequat interdum nisi fusce cras rhoncus feugiat.\n\nHimenaeos mat'
    'tis commodo suspendisse maecenas cras arcu. Habitasse id facilisi praesent justo molestie felis luctus suspendisse'
    '. Imperdiet ipsum praesent nunc mauris mattis curabitur. Et consectetur morbi auctor feugiat enim ridiculus arcu. '
    'Ultricies magna blandit eget; vivamus sollicitudin nisl proin. Sollicitudin sociosqu et finibus elit vestibulum sa'
    'pien nec odio euismod. Turpis eleifend amet quis auctor cursus. Vehicula pharetra sapien praesent amet purus ante.'
    ' Risus blandit cubilia lorem hendrerit penatibus in magnis.\n\nAmet posuere nunc; maecenas consequat risus potenti'
    '. Volutpat leo lacinia sapien nulla sagittis dignissim mauris ultrices aliquet. Nisi pretium interdum luctus donec'
    ' magna suscipit. Dapibus tristique felis natoque malesuada augue? Justo faucibus tincidunt congue arcu sem; fusce '
    'aliquet proin. Commodo neque nibh; tempus ad tortor netus. Mattis ultricies nec maximus porttitor non mauris?'
)

# Wrapper --------------------------------------------------------------------------------------------------------------

class TextWrapper:

    """ Text wrapper class """

    # Dunder / Magic Methods -------------------------------------------------------------------------------------------

    __slots__ = ('_d',)

    def __init__(self, width=70, line_padding=0, method='word', alignment='left', placeholder='...', fillchar=' ',
                 separator=None, max_lines=None, preserve_empty=True, minimum_width=True, justify_last_line=False,
                 break_on_hyphens=True, sizefunc=None):

        """
        See txtwrap module documentation on [GitHub](https://github.com/azzammuhyala/txtwrap) or on
        [PyPi](https://pypi.org/project/txtwrap) for details.
        """

        # dictionary to store a metadata and private variables
        self._d = pdict()

        self.width = width
        self.line_padding = line_padding
        self.method = method
        self.alignment = alignment
        self.placeholder = placeholder
        self.fillchar = fillchar
        self.separator = separator
        self.max_lines = max_lines
        self.preserve_empty = preserve_empty
        self.minimum_width = minimum_width
        self.justify_last_line = justify_last_line
        self.break_on_hyphens = break_on_hyphens
        self.sizefunc = sizefunc

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(
                '{}={!r}'.format(name, getattr(self, name))
                for name in self.__init__.__code__.co_varnames
                if name != 'self'
            )
        )

    def __str__(self):
        return '<{}.{} object at 0x{}>'.format(
            self.__class__.__module__,
            self.__class__.__name__,
            hex(id(self))[2:].upper().zfill(16)
        )

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo):
        return self.copy()

    # Properties -------------------------------------------------------------------------------------------------------

    @property
    def width(self):
        return self._d.width

    @property
    def line_padding(self):
        return self._d.line_padding

    @property
    def method(self):
        return self._d.method

    @property
    def alignment(self):
        return self._d.alignment

    @property
    def placeholder(self):
        return self._d.placeholder

    @property
    def fillchar(self):
        return self._d.fillchar

    @property
    def separator(self):
        return self._d.separator

    @property
    def max_lines(self):
        return self._d.max_lines

    @property
    def preserve_empty(self):
        return self._d.preserve_empty

    @property
    def minimum_width(self):
        return self._d.minimum_width

    @property
    def justify_last_line(self):
        return self._d.justify_last_line

    @property
    def break_on_hyphens(self):
        return self._d.break_on_hyphens

    @property
    def sizefunc(self):
        return self._d._sizefunc

    # Setters ----------------------------------------------------------------------------------------------------------

    @width.setter
    def width(self, new):
        if not isinstance(new, (int, float)):
            raise TypeError("width must be an integer or float")
        if new <= 0:
            raise ValueError("width must be greater than 0")
        self._d.width = new

    @line_padding.setter
    def line_padding(self, new):
        if not isinstance(new, (int, float)):
            raise TypeError("line_padding must be a integer or float")
        if new < 0:
            raise ValueError("line_padding must be equal to or greater than 0")
        self._d.line_padding = new

    @method.setter
    def method(self, new):
        if not isinstance(new, str):
            raise TypeError("method must be a string")
        new = new.strip().lower()
        if new not in {'mono', 'word'}:
            raise ValueError("method={!r} is invalid, must be 'mono' or 'word'".format(new))
        self._d.method = new
        if new == 'mono':
            self._d.wrapfunc = mono
        elif new == 'word':
            self._d.wrapfunc = word

    @alignment.setter
    def alignment(self, new):
        if not isinstance(new, str):
            raise TypeError("alignment must be a string")
        new = new.strip().lower()
        if new not in {'left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'}:
            raise ValueError("alignment={!r} is invalid, must be 'left', 'center', 'right', 'fill', 'fill-left', "
                             "'fill-center', or 'fill-right'".format(new))
        self._d.alignment = new = 'fill-left' if new == 'fill' else new
        if new.endswith('left'):
            self._d.align_justify = jusitfy_align_left
            self._d.fillstr_justify = justify_fillstr_left
        elif new.endswith('center'):
            self._d.align_justify = justify_align_center
            self._d.fillstr_justify = justify_fillstr_center
        elif new.endswith('right'):
            self._d.align_justify = justify_align_right
            self._d.fillstr_justify = justify_fillstr_right

    @placeholder.setter
    def placeholder(self, new):
        if not isinstance(new, str):
            raise TypeError("placeholder must be a string")
        self._d.placeholder = new

    @fillchar.setter
    def fillchar(self, new):
        if not isinstance(new, str):
            raise TypeError("fillchar must be a string")
        self._d.fillchar = new
        split = compile(escape(new)).split
        self._d.split_fillchar = lambda string : [s for s in split(string) if s]

    @separator.setter
    def separator(self, new):
        if not isinstance(new, (str, Iterable, type(None))):
            raise TypeError("separator must be a string, iterable, or None")
        if isinstance(new, Iterable) and not all(isinstance(s, str) for s in new):
            raise ValueError("separator must be an iterable containing of strings")
        self._d.separator = new
        if new is None:
            self._d.split_separator = lambda s : s.split()
            return
        elif isinstance(new, str): 
            split = compile(escape(new)).split
        else:
            split = compile('|'.join(map(escape, new))).split
        self._d.split_separator = lambda string : [s for s in split(string) if s]

    @max_lines.setter
    def max_lines(self, new):
        if not isinstance(new, (int, type(None))):
            raise TypeError("max_lines must be an integer or None")
        if new is not None and new <= 0:
            raise ValueError("max_lines must be greater than 0")
        self._d.max_lines = new

    @preserve_empty.setter
    def preserve_empty(self, new):
        self._d.preserve_empty = bool(new)

    @minimum_width.setter
    def minimum_width(self, new):
        self._d.minimum_width = bool(new)

    @justify_last_line.setter
    def justify_last_line(self, new):
        self._d.justify_last_line = bool(new)

    @break_on_hyphens.setter
    def break_on_hyphens(self, new):
        self._d.break_on_hyphens = bool(new)

    @sizefunc.setter
    def sizefunc(self, new):
        self._d._sizefunc = new
        if new is None:
            self._d.sizefunc = lambda s : (len(s), 1)
            self._d.lenfunc = len
            return
        if not callable(new):
            raise TypeError("sizefunc must be a callable")
        test = new('test')
        if isinstance(test, tuple):
            if len(test) != 2:
                raise ValueError("sizefunc must be returned a tuple of length 2")
            if not isinstance(test[0], (int, float)):
                raise TypeError("sizefunc returned width must be a tuple of two integers or floats")
            if not isinstance(test[1], (int, float)):
                raise TypeError("sizefunc returned height must be a tuple of two integers or floats")
            if test[0] < 0:
                raise ValueError("sizefunc returned width must be equal to or greater than 0")
            if test[1] < 0:
                raise ValueError("sizefunc returned height must be equal to or greater than 0")
            self._d.sizefunc = new
            self._d.lenfunc = lambda s : new(s)[0]
        elif isinstance(test, (int, float)):
            if test < 0:
                raise ValueError("sizefunc (length) must be equal to or greater than 0")
            self._d.sizefunc = None
            self._d.lenfunc = new
        else:
            raise TypeError("sizefunc must be returned a tuple for size or a single value for width (length)")

    # Methods ----------------------------------------------------------------------------------------------------------

    def copy(self):
        return TextWrapper(width=self._d.width, line_padding=self._d.line_padding, method=self._d.method,
                           alignment=self._d.alignment, placeholder=self._d.placeholder, fillchar=self._d.fillchar,
                           separator=self._d.separator, max_lines=self._d.max_lines,
                           preserve_empty=self._d.preserve_empty, minimum_width=self._d.minimum_width,
                           justify_last_line=self._d.justify_last_line, break_on_hyphens=self._d.break_on_hyphens,
                           sizefunc=self._d._sizefunc)

    def sanitize(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        return self._d.fillchar.join(self._d.split_separator(text))

    def wrap(self, text, return_details=False, *, _one_line=False):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        wrapfunc = self._d.wrapfunc
        width = self._d.width
        placeholder = self._d.placeholder
        fillchar = self._d.fillchar
        split_separator = self._d.split_separator
        max_lines = self._d.max_lines
        preserve_empty = self._d.preserve_empty
        break_on_hyphens = self._d.break_on_hyphens
        lenfunc = self._d.lenfunc

        if _one_line:
            max_lines = 1
        else:
            max_lines = self._d.max_lines

        has_max_lines = max_lines is not None

        if has_max_lines and width < lenfunc(placeholder):
            raise ValueError("width must be greater than length of the placeholder")

        wrapped = []
        indiced = set()

        for line in text.splitlines():
            wrapped_line = wrapfunc(line, width, fillchar, break_on_hyphens, lenfunc, self.sanitize, split_separator)

            if wrapped_line:
                wrapped.extend(wrapped_line)
                lines = len(wrapped)

                if has_max_lines and lines <= max_lines:
                    indiced.add(lines - 1)
                elif not has_max_lines:
                    indiced.add(lines - 1)

            elif preserve_empty:
                wrapped.append('')

            if has_max_lines and len(wrapped) > max_lines:
                current_char = ''

                for part in wrapped[max_lines - 1]:
                    if lenfunc(current_char + part + placeholder) > width:
                        break
                    current_char += part

                wrapped[max_lines - 1] = current_char + placeholder
                wrapped = wrapped[:max_lines]
                break

        if return_details:
            return {'wrapped': wrapped, 'indiced': indiced}

        return wrapped

    def align(self, text, return_details=False):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        width = self._d.width
        line_padding = self._d.line_padding
        alignment = self._d.alignment
        justify = self._d.align_justify
        minimum_width = self._d.minimum_width
        sizefunc = self._d.sizefunc

        if sizefunc is None:
            raise TypeError("sizefunc must be a size")

        wrapped_info = self.wrap(text, True)
        wrapped = wrapped_info['wrapped']
        indiced = wrapped_info['indiced']

        aligned = []
        offset_y = 0

        lines_size = [sizefunc(line) for line in wrapped]

        if minimum_width:
            use_width = max(size[0] for size in lines_size) if lines_size else 0
        else:
            use_width = width

        if alignment in {'left', 'center', 'right'}:
            for i, line in enumerate(wrapped):
                width_line, height_line = lines_size[i]
                justify(aligned, line, use_width, width_line, offset_y)
                offset_y += height_line + line_padding

        else:
            split_fillchar = self._d.split_fillchar
            no_fill_last_line = not self._d.justify_last_line
            lines_word = [split_fillchar(line) for line in wrapped]

            if minimum_width and any(len(line) > 1 and not (no_fill_last_line and i in indiced)
                                     for i, line in enumerate(lines_word)):
                use_width = width if wrapped else 0

            for i, line in enumerate(wrapped):
                width_line, height_line = lines_size[i]

                if no_fill_last_line and i in indiced:
                    justify(aligned, line, use_width, width_line, offset_y)

                else:
                    words = lines_word[i]
                    total_words = len(words)

                    if total_words > 1:
                        all_word_width = [sizefunc(word)[0] for word in words]
                        extra_space = width - sum(all_word_width)
                        space_between_words = extra_space / (total_words - 1)
                        offset_x = 0

                        for j, word in enumerate(words):
                            aligned.append((offset_x, offset_y, word))
                            offset_x += all_word_width[j] + space_between_words
                    else:
                        justify(aligned, line, use_width, width_line, offset_y)

                offset_y += height_line + line_padding

        if return_details:
            return {'aligned': aligned, 'wrapped': wrapped, 'indiced': indiced,
                    'size': (use_width, offset_y - line_padding)}

        return aligned

    def fillstr(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        width = self._d.width
        line_padding = self._d.line_padding
        alignment = self._d.alignment
        fillchar = self._d.fillchar
        justify = self._d.fillstr_justify
        minimum_width = self._d.minimum_width
        lenfunc = self._d.lenfunc

        wrapped_info = self.wrap(text, True)
        wrapped = wrapped_info['wrapped']
        indiced = wrapped_info['indiced']

        justified_lines = []

        lines_width = [lenfunc(line) for line in wrapped]
        add_padding = line_padding > 0

        if minimum_width:
            use_width = max(lines_width) if lines_width else 0
        else:
            use_width = width

        if alignment in {'left', 'center', 'right'}:
            fill_line_padding = '\n'.join(fillchar * use_width for _ in range(line_padding))

            for i, line in enumerate(wrapped):
                justify(justified_lines, line, use_width, lines_width[i], fillchar)
                if add_padding:
                    justified_lines.append(fill_line_padding)

        else:
            split_fillchar = self._d.split_fillchar
            no_fill_last_line = not self._d.justify_last_line
            lines_word = [split_fillchar(line) for line in wrapped]

            if minimum_width and any(len(line) > 1 and not (no_fill_last_line and i in indiced)
                                     for i, line in enumerate(lines_word)):
                use_width = width if wrapped else 0

            fill_line_padding = '\n'.join(fillchar * use_width for _ in range(line_padding))

            for i, line in enumerate(wrapped):

                if no_fill_last_line and i in indiced:
                    justify(justified_lines, line, use_width, lines_width[i], fillchar)

                else:
                    words = lines_word[i]
                    total_words = len(words)

                    if total_words > 1:
                        extra_space = width - sum(lenfunc(w) for w in words)
                        space_between_words = extra_space // (total_words - 1)
                        extra_padding = extra_space % (total_words - 1)
                        justified_line = ''

                        for i, word in enumerate(words):
                            justified_line += word
                            if i < total_words - 1:
                                justified_line += fillchar * (space_between_words + (1 if i < extra_padding else 0))

                        if justified_line:
                            justified_lines.append(justified_line)
                        else:
                            justified_lines.append(fillchar * width)
                    else:
                        justify(justified_lines, line, use_width, lines_width[i], fillchar)

                if add_padding:
                    justified_lines.append(fill_line_padding)

        if add_padding and justified_lines:
            justified_lines.pop()

        return '\n'.join(justified_lines)

    def shorten(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        wrapped = self.wrap(text, _one_line=True)
        return wrapped[0] if wrapped else ''

# Interfaces -----------------------------------------------------------------------------------------------------------

def sanitize(text, fillchar=' ', separator=None):
    return TextWrapper(fillchar=fillchar, separator=separator).sanitize(text)

def wrap(text, width=70, method='word', placeholder='...', fillchar=' ', separator=None, max_lines=None,
         preserve_empty=True, break_on_hyphens=True, return_details=False, sizefunc=None):
    return TextWrapper(width=width, method=method, fillchar=fillchar, placeholder=placeholder, separator=separator,
                       max_lines=max_lines, preserve_empty=preserve_empty, break_on_hyphens=break_on_hyphens,
                       sizefunc=sizefunc).wrap(text, return_details)

def align(text, width=70, line_padding=0, method='word', alignment='left', placeholder='...', fillchar=' ',
          separator=None, max_lines=None, preserve_empty=True, minimum_width=True, justify_last_line=False,
          break_on_hyphens=True, return_details=False, sizefunc=None):
    return TextWrapper(width=width, line_padding=line_padding, method=method, alignment=alignment, fillchar=fillchar,
                       placeholder=placeholder, separator=separator, max_lines=max_lines, preserve_empty=preserve_empty,
                       minimum_width=minimum_width, justify_last_line=justify_last_line,
                       break_on_hyphens=break_on_hyphens, sizefunc=sizefunc).align(text, return_details)

def fillstr(text, width=70, line_padding=0, method='word', alignment='left', placeholder='...', fillchar=' ',
            separator=None, max_lines=None, preserve_empty=True, minimum_width=True, justify_last_line=False,
            break_on_hyphens=True, sizefunc=None):
    return TextWrapper(width=width, line_padding=line_padding, method=method, alignment=alignment, fillchar=fillchar,
                       placeholder=placeholder, separator=separator, max_lines=max_lines, preserve_empty=preserve_empty,
                       minimum_width=minimum_width, justify_last_line=justify_last_line,
                       break_on_hyphens=break_on_hyphens, sizefunc=sizefunc).fillstr(text)

def shorten(text, width=70, method='word', fillchar=' ', placeholder='...', separator=None, sizefunc=None):
    return TextWrapper(width=width, method=method, fillchar=fillchar, placeholder=placeholder, separator=separator,
                       sizefunc=sizefunc).shorten(text)
