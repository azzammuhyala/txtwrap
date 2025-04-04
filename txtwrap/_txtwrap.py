from collections.abc import Iterable, Sequence
from os import get_terminal_size
from re import compile

# Tools --------------------------------------------------------------------------------------------

hyphenated_re = compile(r'(?<=-)(?=(?!-).)')
sentinel = object()  # default object replacement of None

def jusitfy_align_left(aligned_positions, text, width, text_width, offset_y):
    aligned_positions.append((0, offset_y, text))

def justify_align_center(aligned_positions, text, width, text_width, offset_y):
    aligned_positions.append(((width - text_width) / 2, offset_y, text))

def justify_align_right(aligned_positions, text, width, text_width, offset_y):
    aligned_positions.append((width - text_width, offset_y, text))

def justify_fillstr_left(justified_lines, text, width, text_width, fillchar):
    justified_lines.append(
        text +
        fillchar * (width - text_width)
    )

def justify_fillstr_center(justified_lines, text, width, text_width, fillchar):
    extra_space = width - text_width
    left_space = extra_space // 2
    justified_lines.append(
        fillchar * left_space +
        text +
        fillchar * (extra_space - left_space)
    )

def justify_fillstr_right(justified_lines, text, width, text_width, fillchar):
    justified_lines.append(
        fillchar * (width - text_width) +
        text
    )

# Identities ---------------------------------------------------------------------------------------

__version__ = '2.2.0'
__author__ = 'azzammuhyala'
__license__ = 'MIT'

# Constants ----------------------------------------------------------------------------------------

LOREM_IPSUM_WORDS = 'Lorem ipsum odor amet, consectetuer adipiscing elit.'
LOREM_IPSUM_SENTENCES = (
    'Lorem ipsum odor amet, consectetuer adipiscing elit. In malesuada eros natoque urna felis '
    'diam aptent donec. Cubilia libero morbi fusce tempus, luctus aenean augue. Mus senectus '
    'rutrum phasellus fusce dictum platea. Eros a integer nec fusce erat urna.'
)
LOREM_IPSUM_PARAGRAPHS = (
    'Lorem ipsum odor amet, consectetuer adipiscing elit. Nulla porta ex condimentum velit '
    'facilisi; consequat congue. Tristique duis sociosqu aliquam semper sit id. Nisi morbi purus, '
    'nascetur elit pellentesque venenatis. Velit commodo molestie potenti placerat faucibus '
    'convallis. Himenaeos dapibus ipsum natoque nam dapibus habitasse diam. Viverra ac porttitor '
    'cras tempor cras. Pharetra habitant nibh dui ipsum scelerisque cras? Efficitur phasellus '
    'etiam congue taciti tortor quam. Volutpat quam vulputate condimentum hendrerit justo congue '
    'iaculis nisl nullam.\n\nInceptos tempus nostra fringilla arcu; tellus blandit facilisi risus. '
    'Platea bibendum tristique lectus nunc placerat id aliquam. Eu arcu nisl mattis potenti '
    'elementum. Dignissim vivamus montes volutpat litora felis fusce ultrices. Vulputate magna '
    'nascetur bibendum inceptos scelerisque morbi posuere. Consequat dolor netus augue augue '
    'tristique curabitur habitasse bibendum. Consectetur est per eros semper, magnis interdum '
    'libero. Arcu adipiscing litora metus fringilla varius gravida congue tellus adipiscing. '
    'Blandit nulla mauris nullam ante metus curae scelerisque.\n\nSem varius sodales ut volutpat '
    'imperdiet turpis primis nullam. At gravida tincidunt phasellus lacus duis integer eros '
    'penatibus. Interdum mauris molestie posuere nascetur dignissim himenaeos; magna et quisque. '
    'Dignissim malesuada etiam donec vehicula aliquet bibendum. Magna dapibus sapien semper '
    'parturient id dis? Pretium orci ante leo, porta tincidunt molestie. Malesuada dictumst '
    'commodo consequat interdum nisi fusce cras rhoncus feugiat.\n\nHimenaeos mattis commodo '
    'suspendisse maecenas cras arcu. Habitasse id facilisi praesent justo molestie felis luctus '
    'suspendisse. Imperdiet ipsum praesent nunc mauris mattis curabitur. Et consectetur morbi '
    'auctor feugiat enim ridiculus arcu. Ultricies magna blandit eget; vivamus sollicitudin nisl '
    'proin. Sollicitudin sociosqu et finibus elit vestibulum sapien nec odio euismod. Turpis '
    'eleifend amet quis auctor cursus. Vehicula pharetra sapien praesent amet purus ante. Risus '
    'blandit cubilia lorem hendrerit penatibus in magnis.\n\nAmet posuere nunc; maecenas consequat '
    'risus potenti. Volutpat leo lacinia sapien nulla sagittis dignissim mauris ultrices aliquet. '
    'Nisi pretium interdum luctus donec magna suscipit. Dapibus tristique felis natoque malesuada '
    'augue? Justo faucibus tincidunt congue arcu sem; fusce aliquet proin. Commodo neque nibh; '
    'tempus ad tortor netus. Mattis ultricies nec maximus porttitor non mauris?'
)

# Wrapper ------------------------------------------------------------------------------------------

class TextWrapper:

    """ A class for text wrapping. """

    __slots__ = ('_d',)

    def __init__(self, width=70, line_padding=0, method='word', alignment='left', fillchar=' ',
                 placeholder='...', prefix=None, separator=None, max_lines=None,
                 preserve_empty=True, use_minimum_width=True, justify_last_line=False,
                 break_on_hyphens=True, sizefunc=None, predicate=None):

        """
        See txtwrap module documentation on [GitHub](https://github.com/azzammuhyala/txtwrap) or on
        [PyPi](https://pypi.org/project/txtwrap) for details.
        """

        self._d = {}  # dictionary to store a metadata and private variables

        self.width = width
        self.line_padding = line_padding
        self.method = method
        self.alignment = alignment
        self.fillchar = fillchar
        self.sizefunc = sizefunc  # placeholder need this property to be set first
        self.placeholder = placeholder
        self.prefix = prefix
        self.separator = separator
        self.max_lines = max_lines
        self.preserve_empty = preserve_empty
        self.use_minimum_width = use_minimum_width
        self.justify_last_line = justify_last_line
        self.break_on_hyphens = break_on_hyphens
        self.predicate = predicate

    def __repr__(self):
        return 'TextWrapper(' + ', '.join(
            '{}={}'.format(name, repr(getattr(self, name)))
            for name in self.__init__.__code__.co_varnames#[:self.__init__.__code__.co_argcount]
            if name != 'self'
        ) + ')'

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo):
        return self.copy()

    # Properties -----------------------------------------------------------------------------------

    @property
    def width(self):
        return self._d['width']

    @property
    def line_padding(self):
        return self._d['line_padding']

    @property
    def method(self):
        return self._d['method']

    @property
    def alignment(self):
        return self._d['alignment']

    @property
    def fillchar(self):
        return self._d['fillchar']

    @property
    def placeholder(self):
        return self._d['placeholder']

    @property
    def prefix(self):
        return self._d['prefix']

    @property
    def separator(self):
        return self._d['separator']

    @property
    def max_lines(self):
        return self._d['max_lines']

    @property
    def preserve_empty(self):
        return self._d['preserve_empty']

    @property
    def use_minimum_width(self):
        return self._d['use_minimum_width']

    @property
    def justify_last_line(self):
        return self._d['justify_last_line']

    @property
    def break_on_hyphens(self):
        return self._d['break_on_hyphens']

    @property
    def sizefunc(self):
        return self._d['sizefunc']

    @property
    def predicate(self):
        return self._d['predicate']

    # Setters --------------------------------------------------------------------------------------

    @width.setter
    def width(self, new):
        if not isinstance(new, (int, float)):
            raise TypeError("width must be an integer or float")
        if new <= 0:
            raise ValueError("width must be greater than 0")
        if self._d.get('max_lines', None) is not None and new < self._d.get('length_placeholder',
                                                                            new + 1):
            raise ValueError("width must be greater than length of the placeholder")
        self._d['width'] = new

    @line_padding.setter
    def line_padding(self, new):
        if not isinstance(new, (int, float)):
            raise TypeError("line_padding must be a integer or float")
        if new < 0:
            raise ValueError("line_padding must be equal to or greater than 0")
        self._d['line_padding'] = new

    @method.setter
    def method(self, new):
        if not isinstance(new, str):
            raise TypeError("method must be a string")
        new = new.strip().lower()
        if new not in {'mono', 'word'}:
            raise ValueError("method={} is invalid, must be 'mono' or 'word'".format(new))
        self._d['method'] = new
        if new == 'mono':
            self._d['wrapfunc'] = self.mono
        elif new == 'word':
            self._d['wrapfunc'] = self.word

    @alignment.setter
    def alignment(self, new):
        if not isinstance(new, str):
            raise TypeError("alignment must be a string")
        new = new.strip().lower()
        if new not in {'left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'}:
            raise ValueError("alignment={} is invalid, must be 'left', 'center', 'right', "
                             "'fill', 'fill-left', 'fill-center', or 'fill-right'".format(new))
        self._d['alignment'] = new = 'fill-left' if new == 'fill' else new
        if new.endswith('left'):
            self._d['align_justify'] = jusitfy_align_left
            self._d['fillstr_justify'] = justify_fillstr_left
        elif new.endswith('center'):
            self._d['align_justify'] = justify_align_center
            self._d['fillstr_justify'] = justify_fillstr_center
        elif new.endswith('right'):
            self._d['align_justify'] = justify_align_right
            self._d['fillstr_justify'] = justify_fillstr_right

    @fillchar.setter
    def fillchar(self, new):
        if not isinstance(new, str):
            raise TypeError("fillchar must be a string")
        self._d['fillchar'] = new

    @placeholder.setter
    def placeholder(self, new):
        if not isinstance(new, str):
            raise TypeError("placeholder must be a string")
        self._d['placeholder'] = new
        self._d['length_placeholder'] = length = self._d['lenfunc'](new)
        if self._d.get('max_lines', None) is not None and self._d['width'] < length:
            raise ValueError("width must be greater than length of the placeholder")

    @prefix.setter
    def prefix(self, new):
        if not isinstance(new, (str, Iterable, type(None))):
            raise TypeError("prefix must be a string, iterable, or None")
        if isinstance(new, Iterable) and not all(isinstance(s, str) and len(s) == 1 for s in new):
            raise ValueError("prefix must be an iterable containing of strings with only "
                             "1 character")
        self._d['prefix'] = new

    @separator.setter
    def separator(self, new):
        if not isinstance(new, (str, Iterable, type(None))):
            raise TypeError("separator must be a string, iterable, or None")
        if (isinstance(new, Iterable) and not all(isinstance(s, str) and len(s) == 1 for s in new)):
            raise ValueError("separator must be an iterable containing of strings with only "
                             "1 character")
        self._d['separator'] = new

    @max_lines.setter
    def max_lines(self, new):
        if not isinstance(new, (int, type(None))):
            raise TypeError("max_lines must be an integer or None")
        if new is not None:
            if new <= 0:
                raise ValueError("max_lines must be greater than 0")
            if self._d['width'] < self._d['length_placeholder']:
                raise ValueError("width must be greater than length of the placeholder")
        self._d['max_lines'] = new

    @preserve_empty.setter
    def preserve_empty(self, new):
        self._d['preserve_empty'] = new

    @use_minimum_width.setter
    def use_minimum_width(self, new):
        self._d['use_minimum_width'] = new

    @justify_last_line.setter
    def justify_last_line(self, new):
        self._d['justify_last_line'] = new

    @break_on_hyphens.setter
    def break_on_hyphens(self, new):
        self._d['break_on_hyphens'] = new

    @sizefunc.setter
    def sizefunc(self, new):
        if new is None:
            self._d['sizefunc'] = None
            self._d['use_sizefunc'] = lambda s : (len(s), 1)
            self._d['lenfunc'] = len
            return
        if not callable(new):
            raise TypeError("sizefunc must be a callable")
        test = new('test')
        if not isinstance(test, tuple):
            raise TypeError("sizefunc must be returned a tuple")
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
        self._d['sizefunc'] = self._d['use_sizefunc'] = new
        self._d['lenfunc'] = lambda s : new(s)[0]

    @predicate.setter
    def predicate(self, new):
        if new is None:
            self._d['predicate'] = None
            self._d['use_predicate'] = lambda s : s.strip()
            return
        if not callable(new):
            raise TypeError("predicate must be a callable")
        new('test')
        self._d['predicate'] = self._d['use_predicate'] = new

    # Private Methods ------------------------------------------------------------------------------

    def _split(self, text, separator=sentinel):
        if separator is sentinel:
            separator = self._d['separator']

        if separator is None:
            return text.split()

        elif isinstance(separator, str):
            return [s for s in text.split(separator) if s]

        splited = []
        temp = ''

        for char in text:
            if char in separator:
                if temp:
                    splited.append(temp)
                    temp = ''
            else:
                temp += char

        if temp:
            splited.append(temp)

        return splited

    def _sanitize(self, text, separator=sentinel):
        return self._d['fillchar'].join(self._split(text, separator))

    def _finalize_line(self, lines):
        width = self._d['width']
        placeholder = self._d['placeholder']
        max_lines = self._d['max_lines']
        lenfunc = self._d['lenfunc']

        current_char = ''

        for part in lines[max_lines - 1]:
            if lenfunc(current_char + part + placeholder) > width:
                break
            current_char += part

        lines[max_lines - 1] = current_char + placeholder

        return lines[:max_lines]

    # Methods --------------------------------------------------------------------------------------

    def copy(self):
        return TextWrapper(
            width=self._d['width'],
            line_padding=self._d['line_padding'],
            method=self._d['method'],
            alignment=self._d['alignment'],
            fillchar=self._d['fillchar'],
            placeholder=self._d['placeholder'],
            prefix=self._d['prefix'],
            separator=self._d['separator'],
            max_lines=self._d['max_lines'],
            preserve_empty=self._d['preserve_empty'],
            use_minimum_width=self._d['use_minimum_width'],
            justify_last_line=self._d['justify_last_line'],
            break_on_hyphens=self._d['break_on_hyphens'],
            sizefunc=self._d['sizefunc'],
            predicate=self._d['predicate']
        )

    def mono(self, text, *, _recognize_max_lines=True):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        width = self._d['width']
        max_lines = self._d['max_lines']
        lenfunc = self._d['lenfunc']

        set_max_lines = _recognize_max_lines and max_lines is not None

        parts = []
        current_char = ''
        add_last_part = True

        for char in self._sanitize(text):
            if lenfunc(current_char + char) <= width:
                current_char += char
            else:
                parts.append(current_char)
                current_char = char

            if set_max_lines and len(parts) >= max_lines:
                parts = self._finalize_line(parts)
                add_last_part = False
                break

        if add_last_part and current_char:
            parts.append(current_char)

        return parts

    def word(self, text, *, _recognize_max_lines=True):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        width = self._d['width']
        fillchar = self._d['fillchar']
        max_lines = self._d['max_lines']
        break_on_hyphens = self._d['break_on_hyphens']
        lenfunc = self._d['lenfunc']

        set_max_lines = _recognize_max_lines and max_lines is not None

        lines = []
        current_line = ''
        add_last_part = True

        for word in self._split(text):
            test_line = current_line + fillchar + word if current_line else word

            if lenfunc(test_line) <= width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)

                current_line = ''

                if break_on_hyphens:
                    for part in hyphenated_re.split(word):
                        for wrapped_part in self.mono(part):
                            if lenfunc(current_line + wrapped_part) <= width:
                                current_line += wrapped_part
                            else:
                                if current_line:
                                    lines.append(current_line)
                                current_line = wrapped_part

                else:
                    for part in self.mono(word):
                        if lenfunc(current_line + part) <= width:
                            current_line += part
                        else:
                            if current_line:
                                lines.append(current_line)
                            current_line = part

            if set_max_lines and len(lines) >= max_lines:
                lines = self._finalize_line(lines)
                add_last_part = False
                break

        if add_last_part and current_line:
            lines.append(current_line)

        return lines

    def wrap(self, text, return_details=False):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        preserve_empty = self._d['preserve_empty']
        wrapfunc = self._d['wrapfunc']
        max_lines = self._d['max_lines']

        set_max_lines = max_lines is not None

        wrapped_lines = []
        line_indices = set()

        for line in text.splitlines():
            wrapped_line = wrapfunc(line, _recognize_max_lines=False)

            if wrapped_line:
                wrapped_lines.extend(wrapped_line)
                lines = len(wrapped_lines)

                if set_max_lines and lines <= max_lines:
                    line_indices.add(lines - 1)
                elif not set_max_lines:
                    line_indices.add(lines - 1)

            elif preserve_empty:
                wrapped_lines.append('')

            if set_max_lines and len(wrapped_lines) > max_lines:
                wrapped_lines = self._finalize_line(wrapped_lines)
                break

        if return_details:
            return {
                'wrapped': wrapped_lines,
                'indiced': line_indices
            }

        return wrapped_lines

    def align(self, text, return_details=False):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        width = self._d['width']
        line_padding = self._d['line_padding']
        alignment = self._d['alignment']
        justify = self._d['align_justify']
        fillchar = self._d['fillchar']
        use_minimum_width = self._d['use_minimum_width']
        sizefunc = self._d['use_sizefunc']

        wrap_info = self.wrap(text, True)

        wrapped = wrap_info['wrapped']
        line_indiced = wrap_info['indiced']

        aligned_positions = []
        offset_y = 0

        lines_size = {i: sizefunc(line) for i, line in enumerate(wrapped)}

        if use_minimum_width:
            use_width = max(size[0] for size in lines_size.values())
        else:
            use_width = width

        if alignment in {'left', 'center', 'right'}:
            for i, line in enumerate(wrapped):
                width_line, height_line = lines_size[i]

                justify(
                    aligned_positions,
                    line,
                    use_width,
                    width_line,
                    offset_y
                )

                offset_y += height_line + line_padding

        else:
            lines_word = {i: self._split(line, fillchar) for i, line in enumerate(wrapped)}
            no_fill_last_line = not self._d['justify_last_line']

            if use_minimum_width and any(
                    len(line) > 1 and not (no_fill_last_line and i in line_indiced)
                    for i, line in enumerate(lines_word.values())
                ): use_width = width if wrapped else 0

            for i, line in enumerate(wrapped):
                width_line, height_line = lines_size[i]

                if no_fill_last_line and i in line_indiced:
                    justify(
                        aligned_positions,
                        line,
                        use_width,
                        width_line,
                        offset_y
                    )

                else:
                    words = lines_word[i]
                    total_words = len(words)

                    if total_words > 1:
                        all_word_width = {j: sizefunc(w)[0] for j, w in enumerate(words)}
                        extra_space = width - sum(all_word_width.values())
                        space_between_words = extra_space / (total_words - 1)
                        offset_x = 0

                        for j, w in enumerate(words):
                            aligned_positions.append((offset_x, offset_y, w))
                            offset_x += all_word_width[j] + space_between_words

                    else:
                        justify(
                            aligned_positions,
                            line,
                            use_width,
                            width_line,
                            offset_y
                        )

                offset_y += height_line + line_padding

        if return_details:
            return {
                'aligned': aligned_positions,
                'wrapped': wrapped,
                'indiced': line_indiced,
                'size': (use_width, offset_y - line_padding)
            }

        return aligned_positions

    def fillstr(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        width = self._d['width']
        line_padding = self._d['line_padding']
        alignment = self._d['alignment']
        fillchar = self._d['fillchar']
        justify = self._d['fillstr_justify']
        use_minimum_width = self._d['use_minimum_width']
        lenfunc = self._d['lenfunc']

        wrap_info = self.wrap(text, True)

        wrapped = wrap_info['wrapped']
        line_indiced = wrap_info['indiced']

        justified_lines = []

        lines_width = {i: lenfunc(line) for i, line in enumerate(wrapped)}
        add_padding = line_padding > 0

        if use_minimum_width:
            use_width = max(lines_width.values()) if lines_width else 0
        else:
            use_width = width

        if alignment in {'left', 'center', 'right'}:
            fill_line_padding = '\n'.join(fillchar * use_width for _ in range(line_padding))

            for i, line in enumerate(wrapped):
                justify(
                    justified_lines,
                    line,
                    use_width,
                    lines_width[i],
                    fillchar
                )

                if add_padding:
                    justified_lines.append(fill_line_padding)

        else:
            lines_word = {i: self._split(line, fillchar) for i, line in enumerate(wrapped)}
            no_fill_last_line = not self._d['justify_last_line']

            if use_minimum_width and any(
                    len(line) > 1 and not (no_fill_last_line and i in line_indiced)
                    for i, line in enumerate(lines_word.values())
                ): use_width = width if wrapped else 0

            fill_line_padding = '\n'.join(fillchar * use_width for _ in range(line_padding))

            for i, line in enumerate(wrapped):

                if no_fill_last_line and i in line_indiced:
                    justify(
                        justified_lines,
                        line,
                        use_width,
                        lines_width[i],
                        fillchar
                    )

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
                                justified_line += fillchar * (space_between_words +
                                                              (1 if i < extra_padding else 0))

                        if justified_line:
                            justified_lines.append(justified_line)
                        else:
                            justified_lines.append(fillchar * width)

                    else:
                        justify(
                            justified_lines,
                            line,
                            use_width,
                            lines_width[i],
                            fillchar
                        )

                if add_padding:
                    justified_lines.append(fill_line_padding)

        if add_padding and justified_lines:
            justified_lines.pop()

        return '\n'.join(justified_lines)

    def indent(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        prefix = self._d['prefix']
        predicate = self._d['use_predicate']

        if prefix is None:
            raise ValueError("prefix require")
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")

        indented = []

        for line in text.splitlines():
            line = self._sanitize(line)
            if predicate(line):
                indented.append(prefix + line)

        return '\n'.join(indented)

    def dedent(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        prefix = self._d['prefix']
        predicate = self._d['use_predicate']

        is_prefix_iterable = isinstance(prefix, Iterable)

        dedented = []

        for line in text.splitlines():
            line = self._sanitize(line)

            if predicate(line):
                if is_prefix_iterable:
                    i = 0
                    len_line = len(line)

                    while i < len_line and line[i] in prefix:
                        i += 1

                    line = line[i:]
                else:
                    line = line.lstrip(prefix)

                dedented.append(line)

        return '\n'.join(dedented)

    def shorten(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        temp_max_lines = self._d['max_lines']

        self.max_lines = 1

        wrap = self.wrap(text)

        self._d['max_lines'] = temp_max_lines

        return wrap[0] if wrap else ''

# Interfaces ---------------------------------------------------------------------------------------

def mono(text, width=70, fillchar=' ', placeholder='...', separator=None, max_lines=None,
         lenfunc=None):
    return TextWrapper(
        width=width,
        fillchar=fillchar,
        placeholder=placeholder,
        separator=separator,
        max_lines=max_lines,
        sizefunc=None if lenfunc is None else lambda s : (lenfunc(s), 1)
    ).mono(text)

def word(text, width=70, fillchar=' ', placeholder='...', separator=None, max_lines=None,
         break_on_hyphens=True, lenfunc=None):
    return TextWrapper(
        width=width,
        fillchar=fillchar,
        placeholder=placeholder,
        separator=separator,
        max_lines=max_lines,
        break_on_hyphens=break_on_hyphens,
        sizefunc=None if lenfunc is None else lambda s : (lenfunc(s), 1)
    ).word(text)

def wrap(text, width=70, method='word', fillchar=' ', placeholder='...', separator=None,
         max_lines=None, preserve_empty=True, break_on_hyphens=True, return_details=False,
         lenfunc=None):
    return TextWrapper(
        width=width,
        method=method,
        fillchar=fillchar,
        placeholder=placeholder,
        separator=separator,
        max_lines=max_lines,
        preserve_empty=preserve_empty,
        break_on_hyphens=break_on_hyphens,
        sizefunc=None if lenfunc is None else lambda s : (lenfunc(s), 1),
    ).wrap(text, return_details)

def align(text, width=70, line_padding=0, method='word', alignment='left', fillchar=' ',
          placeholder='...', separator=None, max_lines=None, preserve_empty=True,
          use_minimum_width=True, justify_last_line=False, break_on_hyphens=True,
          return_details=False, sizefunc=None):
    return TextWrapper(
        width=width,
        line_padding=line_padding,
        method=method,
        alignment=alignment,
        fillchar=fillchar,
        placeholder=placeholder,
        separator=separator,
        max_lines=max_lines,
        preserve_empty=preserve_empty,
        use_minimum_width=use_minimum_width,
        justify_last_line=justify_last_line,
        break_on_hyphens=break_on_hyphens,
        sizefunc=sizefunc
    ).align(text, return_details)

def fillstr(text, width=70, line_padding=0, method='word', alignment='left', fillchar=' ',
            placeholder='...', separator=None, max_lines=None, preserve_empty=True,
            use_minimum_width=True, justify_last_line=False, break_on_hyphens=True, lenfunc=None):
    return TextWrapper(
        width=width,
        line_padding=line_padding,
        method=method,
        alignment=alignment,
        fillchar=fillchar,
        placeholder=placeholder,
        separator=separator,
        max_lines=max_lines,
        preserve_empty=preserve_empty,
        use_minimum_width=use_minimum_width,
        justify_last_line=justify_last_line,
        break_on_hyphens=break_on_hyphens,
        sizefunc=None if lenfunc is None else lambda s : (lenfunc(s), 1)
    ).fillstr(text)

def printwrap(*values, sep=' ', end='\n', wrap=None, file=None, flush=False, size=None,
              default_size=(70, None), apply_height=True, use_minimum_width=False, **kwargs):

    auto = isinstance(size, str) and size.strip().lower() == 'auto'
    text = (' ' if sep is None else sep).join(map(str, values))

    if size is None or auto:
        try:
            width, height = get_terminal_size()
        except:
            width, height = default_size
    elif isinstance(size, Sequence):
        width, height = size
    else:
        width, height = default_size

    if not apply_height:
        height = None

    if width <= 0 or (height and height <= 0):
        return

    if wrap is None:
        string = fillstr(
            text,
            width=width,
            max_lines=height,
            use_minimum_width=use_minimum_width,
            **kwargs
        )
    elif isinstance(wrap, TextWrapper):
        if auto:
            wrap.width = width
            wrap.line_padding = 0
            wrap.max_lines = height
        string = wrap.fillstr(text)
    else:
        raise TypeError("wrap argument must be a TextWrapper instance or None")

    print(string, end=end, file=file, flush=flush)

def indent(text, prefix, predicate=None, fillchar=' ', separator=None):
    return TextWrapper(
        fillchar=fillchar,
        prefix=prefix,
        separator=separator,
        predicate=predicate
    ).indent(text)

def dedent(text, prefix=None, predicate=None, fillchar=' ', separator=None):
    return TextWrapper(
        fillchar=fillchar,
        prefix=prefix,
        separator=separator,
        predicate=predicate
    ).dedent(text)

def shorten(text, width=70, method='word', fillchar=' ', placeholder='...', separator=None,
            lenfunc=None):
    return TextWrapper(
        width=width,
        method=method,
        fillchar=fillchar,
        placeholder=placeholder,
        separator=separator,
        sizefunc=None if lenfunc is None else lambda s : (lenfunc(s), 1)
    ).shorten(text)
