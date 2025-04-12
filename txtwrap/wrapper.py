import re

from .constants import SEPARATOR_WHITESPACE
from . import _utils

class TextWrapper:

    """ Text wrapper class """

    __slots__ = ('_d',)

    def __init__(self, width=70, line_padding=0, mode='word', alignment='left', placeholder='...', fillchar=' ',
                 separator=None, max_lines=None, preserve_empty_lines=True, minimum_width=True, justify_last_line=False,
                 break_on_hyphens=True, drop_separator=False, sizefunc=None):

        """
        See txtwrap module documentation on [GitHub](https://github.com/azzammuhyala/txtwrap) or on
        [PyPi](https://pypi.org/project/txtwrap) for details.
        """

        # dictionary to store a metadata and private variables
        self._d = _utils.pdict()

        self.width = width
        self.line_padding = line_padding
        self.mode = mode
        self.alignment = alignment
        self.placeholder = placeholder
        self.fillchar = fillchar
        self.separator = separator
        self.max_lines = max_lines
        self.preserve_empty_lines = preserve_empty_lines
        self.minimum_width = minimum_width
        self.justify_last_line = justify_last_line
        self.break_on_hyphens = break_on_hyphens
        self.drop_separator = drop_separator
        self.sizefunc = sizefunc

    def __repr__(self):
        return '{}({})'.format(
            type(self).__name__,
            ', '.join(
                '{}={!r}'.format(
                    name,
                    getattr(self, name, None)  # if did't find the attribute, use the default None
                )
                for i, name in enumerate(self.__init__.__code__.co_varnames)
                if i != 0  # skip self
            )
        )

    def __str__(self):
        return '<{}.{} object at 0x{}>'.format(
            type(self).__module__,
            type(self).__name__,
            hex(id(self))[2:].upper().zfill(16)
        )

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo):
        return self.copy()

    @property
    def width(self):
        return self._d.width

    @property
    def line_padding(self):
        return self._d.line_padding

    @property
    def mode(self):
        return self._d.mode

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
    def preserve_empty_lines(self):
        return self._d.preserve_empty_lines

    @property
    def minimum_width(self):
        return self._d.minimum_width

    @property
    def drop_separator(self):
        return self._d.drop_separator

    @property
    def justify_last_line(self):
        return self._d.justify_last_line

    @property
    def break_on_hyphens(self):
        return self._d.break_on_hyphens

    @property
    def sizefunc(self):
        # _sizefunc pure parameter of setter so it can return any value not function
        return self._d._sizefunc

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

    @mode.setter
    def mode(self, new):
        if not isinstance(new, str):
            raise TypeError("mode must be a string")
        new = new.strip().lower()
        if new not in {'mono', 'word'}:
            raise ValueError("mode={!r} is invalid, must be 'mono' or 'word'".format(new))
        self._d.mode = new
        # choose based wrap mode
        if new == 'mono':
            self._d.wrapfunc = self._wrap_mono
        elif new == 'word':
            self._d.wrapfunc = self._wrap_word

    @alignment.setter
    def alignment(self, new):
        if not isinstance(new, str):
            raise TypeError("alignment must be a string")
        new = new.strip().lower()
        if new not in {'left', 'center', 'right', 'fill', 'fill-left', 'fill-center', 'fill-right'}:
            raise ValueError("alignment={!r} is invalid, must be 'left', 'center', 'right', 'fill', 'fill-left', "
                             "'fill-center', or 'fill-right'".format(new))
        self._d.alignment = new = 'fill-left' if new == 'fill' else new
        # choose based justify
        if new.endswith('left'):
            self._d.align_justify = _utils.align_left
            self._d.fillstr_justify = _utils.fillstr_left
        elif new.endswith('center'):
            self._d.align_justify = _utils.align_center
            self._d.fillstr_justify = _utils.fillstr_center
        elif new.endswith('right'):
            self._d.align_justify = _utils.align_right
            self._d.fillstr_justify = _utils.fillstr_right

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
        self._d.split_fillchar = re.compile(re.escape(new)).split

    @separator.setter
    def separator(self, new):
        # collections.abc.Iterable has only been around since version 3.3, so to check the iterable object,
        # check it with iter() manually
        try:
            iterator = iter(new)
            is_iterable = True
        except:
            is_iterable = False
        if not (is_iterable or isinstance(new, (str, type(None)))):
            raise TypeError("separator must be a string, iterable, or None")
        if is_iterable and not all(isinstance(s, str) for s in iterator):
            raise ValueError("separator must be an iterable containing of strings")
        self._d.separator = new
        if new is None:
            new = SEPARATOR_WHITESPACE
        if isinstance(new, str): 
            self._d.split_separator = re.compile(re.escape(new)).split
        else:
            self._d.split_separator = re.compile('|'.join(map(re.escape, new))).split

    @max_lines.setter
    def max_lines(self, new):
        if not isinstance(new, (int, type(None))):
            raise TypeError("max_lines must be an integer or None")
        if new is not None and new <= 0:
            raise ValueError("max_lines must be greater than 0")
        self._d.max_lines = new

    @preserve_empty_lines.setter
    def preserve_empty_lines(self, new):
        self._d.preserve_empty_lines = bool(new)

    @minimum_width.setter
    def minimum_width(self, new):
        self._d.minimum_width = bool(new)

    @drop_separator.setter
    def drop_separator(self, new):
        self._d.drop_separator = bool(new)

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
            # default sizefunc and lenfunc
            self._d.sizefunc = lambda s : (len(s), 1)
            self._d.lenfunc = len
            return
        if not callable(new):
            raise TypeError("sizefunc must be a callable")
        test = new('test')
        if isinstance(test, tuple):
            # case where sizefunc returns a tuple (width, height)
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
            # case where sizefunc returns a integer or float (width / length)
            if test < 0:
                raise ValueError("sizefunc (length) must be equal to or greater than 0")
            self._d.sizefunc = None
            self._d.lenfunc = new
        else:
            raise TypeError("sizefunc must be returned a tuple for size or a single value for width (length)")

    def _split(self, text, splitfunc):
        if self._d.drop_separator:
            # remove empty strings
            return [s for s in splitfunc(text) if s]
        return splitfunc(text)

    def _wrap_mono(self, text):
        width = self._d.width
        lenfunc = self._d.lenfunc

        wrapped = []
        current_char = ''

        for char in self._d.fillchar.join(self._split(text, self._d.split_separator)):
            if lenfunc(current_char + char) <= width:
                current_char += char
            else:
                wrapped.append(current_char)
                current_char = char

        # add last line
        if current_char:
            wrapped.append(current_char)

        return wrapped

    def _wrap_word(self, text):
        width = self._d.width
        fillchar = self._d.fillchar
        break_on_hyphens = self._d.break_on_hyphens
        lenfunc = self._d.lenfunc

        # delete more than one separator character at once (applies to the prefix of the string)
        preserve_leading_separator = not self._d.drop_separator
        first_word_index = None

        wrapped = []
        current_line = ''

        def breaks_long_word(part):
            nonlocal current_line
            for line in self._wrap_mono(part):
                if lenfunc(current_line + line) <= width:
                    current_line += line
                else:
                    if current_line:
                        wrapped.append(current_line)
                    current_line = line

        for i, word in enumerate(self._split(text, self._d.split_separator)):
            # check if preserve_leading_separator is still maintained
            # if yes then check again whether word now contains an empty string or a word
            # if yes then preserve_leading_separator is disabled and save the last index of the word
            if preserve_leading_separator and word:
                preserve_leading_separator = False
                first_word_index = i

            if current_line:
                # does not add additional fillchar if preserve_leading_separator is still enabled
                test_line = current_line + (fillchar + word if first_word_index != i else word)
            else:
                # if current_line is empty then fill it with fillchar if preserve_leading_separator is still enabled
                test_line = fillchar if preserve_leading_separator else word

            if lenfunc(test_line) <= width:
                current_line = test_line
            else:
                # if the row has reached the lower limit then the preserve leading separator is disabled
                preserve_leading_separator = False

                if current_line:
                    wrapped.append(current_line)
                    current_line = ''

                if break_on_hyphens:
                    for part in _utils.split_hyphenated(word):
                        breaks_long_word(part)
                else:
                    breaks_long_word(word)

        if current_line:
            wrapped.append(current_line)

        return wrapped

    def copy(self):
        return TextWrapper(**{
            name: getattr(self, name)
            for i, name in enumerate(self.__init__.__code__.co_varnames)
            if i != 0  # skip self
        })

    def sanitize(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        return self._d.fillchar.join(s for s in self._d.split_separator(text) if s)

    def wrap(self, text, return_details=False, *, _one_line=False):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        wrapfunc = self._d.wrapfunc
        width = self._d.width
        placeholder = self._d.placeholder
        max_lines = self._d.max_lines
        preserve_empty_lines = self._d.preserve_empty_lines
        lenfunc = self._d.lenfunc

        if _one_line:
            max_lines = 1
        else:
            max_lines = self._d.max_lines

        has_max_lines = max_lines is not None

        if has_max_lines and width < lenfunc(placeholder):
            raise ValueError("width must be greater than length of the placeholder")

        wrapped = []
        start_lines = set()
        end_lines = set()

        for line in text.splitlines():
            wrapped_line = wrapfunc(line)

            if wrapped_line:
                start_lines.add(len(wrapped) + 1)  # add 1 line for next wrapped_line were added
                wrapped.extend(wrapped_line)

                nline = len(wrapped)

                if has_max_lines and nline <= max_lines:
                    # only added if it has the max_lines attribute and the current line is no more than max_lines
                    end_lines.add(nline)
                elif not has_max_lines:
                    # if not set
                    end_lines.add(nline)

            elif preserve_empty_lines:
                wrapped.append('')  # adding an empty string (usually occurs when encountering an empty line)

                nline = len(wrapped)

                start_lines.add(nline)
                end_lines.add(nline)

            if has_max_lines and len(wrapped) > max_lines:
                # cut off the excess part of the wrapper and also add a placeholder to indicate that the wrapper has
                # been cut off.
                current_part = ''

                for part in wrapped[max_lines - 1]:
                    if lenfunc(current_part + part + placeholder) > width:
                        break
                    current_part += part

                wrapped[max_lines - 1] = current_part + placeholder
                wrapped = wrapped[:max_lines]

                end_lines.add(max_lines)
                break

        if return_details:
            return {
                'wrapped': wrapped,
                'start_lines': start_lines,
                'end_lines': end_lines
            }

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
        end_lines = wrapped_info['end_lines']

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
            lines_word = [self._split(line, split_fillchar) for line in wrapped]

            if minimum_width and any(len(line) > 1 and not (no_fill_last_line and i in end_lines)
                                     for i, line in enumerate(lines_word, start=1)):
                use_width = width if wrapped else 0

            for i, line in enumerate(wrapped):
                width_line, height_line = lines_size[i]

                if no_fill_last_line and i + 1 in end_lines:
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
            return {
                'aligned': aligned,
                'wrapped': wrapped,
                'start_lines': wrapped_info['start_lines'],
                'end_lines': end_lines,
                'size': (use_width, offset_y - line_padding)
            }

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
        end_lines = wrapped_info['end_lines']

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
            lines_word = [self._split(line, split_fillchar) for line in wrapped]

            if minimum_width and any(len(line) > 1 and not (no_fill_last_line and i in end_lines)
                                     for i, line in enumerate(lines_word, start=1)):
                use_width = width if wrapped else 0

            fill_line_padding = '\n'.join(fillchar * use_width for _ in range(line_padding))

            for i, line in enumerate(wrapped):

                if no_fill_last_line and i + 1 in end_lines:
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
            # remove the last padding line
            justified_lines.pop()

        return '\n'.join(justified_lines)

    def shorten(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        # _one_line parameter to change the wrap behavior of max_lines as if set to 1 line max. If this is set via
        # `self.max_lines = 1` it can cause "race condition"
        wrapped = self.wrap(text, _one_line=True)
        return wrapped[0] if wrapped else ''

def sanitize(text, fillchar=' ', separator=None):
    return TextWrapper(fillchar=fillchar, separator=separator).sanitize(text)

def wrap(text, width=70, mode='word', placeholder='...', fillchar=' ', separator=None, max_lines=None,
         preserve_empty_lines=True, drop_separator=False, break_on_hyphens=True, return_details=False, sizefunc=None):
    return TextWrapper(width=width, mode=mode, fillchar=fillchar, placeholder=placeholder, separator=separator,
                       max_lines=max_lines, preserve_empty_lines=preserve_empty_lines, drop_separator=drop_separator,
                       break_on_hyphens=break_on_hyphens, sizefunc=sizefunc).wrap(text, return_details)

def align(text, width=70, line_padding=0, mode='word', alignment='left', placeholder='...', fillchar=' ',
          separator=None, max_lines=None, preserve_empty_lines=True, minimum_width=True, drop_separator=False,
          justify_last_line=False, break_on_hyphens=True, return_details=False, sizefunc=None):
    return TextWrapper(width=width, line_padding=line_padding, mode=mode, alignment=alignment, fillchar=fillchar,
                       placeholder=placeholder, separator=separator, max_lines=max_lines,
                       preserve_empty_lines=preserve_empty_lines, minimum_width=minimum_width,
                       drop_separator=drop_separator, justify_last_line=justify_last_line,
                       break_on_hyphens=break_on_hyphens, sizefunc=sizefunc).align(text, return_details)

def fillstr(text, width=70, line_padding=0, mode='word', alignment='left', placeholder='...', fillchar=' ',
            separator=None, max_lines=None, preserve_empty_lines=True, minimum_width=True, drop_separator=False,
            justify_last_line=False, break_on_hyphens=True, sizefunc=None):
    return TextWrapper(width=width, line_padding=line_padding, mode=mode, alignment=alignment, fillchar=fillchar,
                       placeholder=placeholder, separator=separator, max_lines=max_lines,
                       preserve_empty_lines=preserve_empty_lines, minimum_width=minimum_width,
                       drop_separator=drop_separator, justify_last_line=justify_last_line,
                       break_on_hyphens=break_on_hyphens, sizefunc=sizefunc).fillstr(text)

def shorten(text, width=70, mode='word', fillchar=' ', placeholder='...', separator=None, drop_separator=True,
            sizefunc=None):
    return TextWrapper(width=width, mode=mode, fillchar=fillchar, placeholder=placeholder, separator=separator,
                       drop_separator=drop_separator, sizefunc=sizefunc).shorten(text)