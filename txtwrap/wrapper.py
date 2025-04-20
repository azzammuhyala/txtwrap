import copy
import re

from .constants import SEPARATOR_WHITESPACE, SEPARATOR_NEWLINE
from . import _utils

class TextWrapper:

    """ Text wrapper class """

    __slots__ = ('_d',)

    def __init__(self, width=70, line_padding=0, mode='word', alignment='left', placeholder='...', space_character=' ',
                 newline_character='\n', word_separator=None, newline_separator=None, max_lines=None, empty_lines=True,
                 minimum_width=True, excess_word_separator=False, justify_last_line=False, break_on_hyphens=True,
                 size_function=None):

        # dictionary to store a metadata and private variables
        self._d = _utils.pdict(
            attributes=self.__init__.__code__.co_varnames[1:],  # skip self
            identity='<{0}.{1} object at 0x{2:016X}>'.format(
                type(self).__module__,
                type(self).__name__,
                id(self)
            )
        )

        self.width = width
        self.line_padding = line_padding
        self.mode = mode
        self.alignment = alignment
        self.placeholder = placeholder
        self.space_character = space_character
        self.newline_character = newline_character
        self.word_separator = word_separator
        self.newline_separator = newline_separator
        self.max_lines = max_lines
        self.empty_lines = empty_lines
        self.minimum_width = minimum_width
        self.excess_word_separator = excess_word_separator
        self.justify_last_line = justify_last_line
        self.break_on_hyphens = break_on_hyphens
        self.size_function = size_function

    def __repr__(self):
        return '{0}({1})'.format(
            type(self).__name__,
            ', '.join(
                '{0}={1}'.format(name, repr(getattr(self, name, _utils.unknown)))
                for name in self._d.attributes
            )
        )

    def __str__(self):
        return self._d.identity

    def __copy__(self):
        return TextWrapper(**{
            name: getattr(self, name)
            for name in self._d.attributes
        })

    def __deepcopy__(self, memo=None):
        return TextWrapper(**{
            name: copy.deepcopy(getattr(self, name), memo)
            for name in self._d.attributes
        })

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
    def space_character(self):
        return self._d.space_character

    @property
    def newline_character(self):
        return self._d.newline_character

    @property
    def word_separator(self):
        return self._d.word_separator

    @property
    def newline_separator(self):
        return self._d.newline_separator

    @property
    def max_lines(self):
        return self._d.max_lines

    @property
    def empty_lines(self):
        return self._d.empty_lines

    @property
    def minimum_width(self):
        return self._d.minimum_width

    @property
    def excess_word_separator(self):
        return self._d.excess_word_separator

    @property
    def justify_last_line(self):
        return self._d.justify_last_line

    @property
    def break_on_hyphens(self):
        return self._d.break_on_hyphens

    @property
    def size_function(self):
        # _size_function pure parameter of setter so it can return any value not function
        return self._d._size_function

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

        # choose based wrap mode
        if new == 'mono':
            self._d.wrap_function = self._wrap_mono
        elif new == 'word':
            self._d.wrap_function = self._wrap_word
        else:
            raise ValueError("mode={0} is invalid, must be 'mono' or 'word'".format(repr(new)))

        self._d.mode = new

    @alignment.setter
    def alignment(self, new):
        if not isinstance(new, str):
            raise TypeError("alignment must be a string")

        new = new.strip().lower()

        self._d.alignment = new = 'fill-left' if new == 'fill' else new

        if new not in {'left', 'center', 'right', 'fill-left', 'fill-center', 'fill-right'}:
            raise ValueError("alignment={0} is invalid, must be 'left', 'center', 'right', 'fill', 'fill-left', "
                             "'fill-center', or 'fill-right'".format(repr(new)))

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

    @space_character.setter
    def space_character(self, new):
        if not isinstance(new, str):
            raise TypeError("space_character must be a string")

        self._d.space_character = new
        self._d.split_space = re.compile(re.escape(new)).split

    @newline_character.setter
    def newline_character(self, new):
        if not isinstance(new, str):
            raise TypeError("newline_character must be a string")

        self._d.newline_character = new

    @word_separator.setter
    def word_separator(self, new):
        self._d.word_separator = new

        if new is None:
            new = SEPARATOR_WHITESPACE

        if isinstance(new, str):
            # pattern only
            self._d.split_word = re.compile(new).split
        elif isinstance(new, tuple):
            # with arguments
            self._d.split_word = re.compile(*new).split
        else:
            raise TypeError("word_separator must be a string, tuple (pattern, flags), or None")

    @newline_separator.setter
    def newline_separator(self, new):
        self._d.newline_separator = new

        if new is None:
            new = SEPARATOR_NEWLINE

        if isinstance(new, str): 
            self._d.split_newline = re.compile(new).split
        elif isinstance(new, tuple):
            self._d.split_newline = re.compile(*new).split
        else:
            raise TypeError("newline_separator must be a string, tuple (pattern, flags) or None")

    @max_lines.setter
    def max_lines(self, new):
        if not isinstance(new, (int, type(None))):
            raise TypeError("max_lines must be an integer or None")
        if new is not None and new <= 0:
            raise ValueError("max_lines must be greater than 0")

        self._d.max_lines = new

    @empty_lines.setter
    def empty_lines(self, new):
        self._d.empty_lines = bool(new)

    @minimum_width.setter
    def minimum_width(self, new):
        self._d.minimum_width = bool(new)

    @excess_word_separator.setter
    def excess_word_separator(self, new):
        self._d.excess_word_separator = bool(new)

    @justify_last_line.setter
    def justify_last_line(self, new):
        self._d.justify_last_line = bool(new)

    @break_on_hyphens.setter
    def break_on_hyphens(self, new):
        self._d.break_on_hyphens = bool(new)

    @size_function.setter
    def size_function(self, new):
        self._d._size_function = new

        if new is None:
            # default size_function and length_function
            self._d.size_function = lambda s : (len(s), 1)
            self._d.length_function = len
            return

        if getattr(new, '__call__', None) is None:
            raise TypeError("size_function must be a callable")

        self._d.size_function, self._d.length_function = _utils.validate_size_function(new, 'test')

    def _split(self, text, splitfunc):
        return splitfunc(text) if self._d.excess_word_separator else [s for s in splitfunc(text) if s]

    def _wrap_mono(self, text):
        width = self._d.width
        length_function = self._d.length_function

        wrapped = []
        current_char = ''

        for char in self._d.space_character.join(self._split(text, self._d.split_word)):
            if length_function(current_char + char) <= width:
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
        space_character = self._d.space_character
        break_on_hyphens = self._d.break_on_hyphens
        length_function = self._d.length_function

        # delete more than one word_separator character at once (applies to the prefix of the string)
        preserve_leading_separator = self._d.excess_word_separator
        first_word_index = None

        wrapped = []
        current_line = ''

        def breaks_long_word(part):
            nonlocal current_line
            for line in self._wrap_mono(part):
                if length_function(current_line + line) <= width:
                    current_line += line
                else:
                    if current_line:
                        wrapped.append(current_line)
                    current_line = line

        for i, word in enumerate(self._split(text, self._d.split_word)):
            # check if preserve_leading_separator is still maintained
            # if yes then check again whether word now contains an empty string or a word
            # if yes then preserve_leading_separator is disabled and save the last index of the word
            if preserve_leading_separator and word:
                preserve_leading_separator = False
                first_word_index = i

            if current_line:
                # does not add additional space_character if preserve_leading_separator is still enabled
                test_line = current_line + (space_character + word if first_word_index != i else word)
            else:
                # if current_line is empty then fill it with space_character if preserve_leading_separator is still
                # enabled
                test_line = space_character if preserve_leading_separator else word

            if length_function(test_line) <= width:
                current_line = test_line
            else:
                # if the row has reached the lower limit then the preserve leading word_separator is disabled
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
        return self.__copy__()

    def wrap(self, text, return_details=False, *, _one_line=False):
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        wrap_function = self._d.wrap_function
        width = self._d.width
        placeholder = self._d.placeholder
        max_lines = self._d.max_lines
        empty_lines = self._d.empty_lines
        length_function = self._d.length_function

        max_lines = 1 if _one_line else self._d.max_lines
        has_max_lines = max_lines is not None

        if has_max_lines and width < length_function(placeholder):
            raise ValueError("width must be greater than length of the placeholder")

        wrapped = []
        start_lines = []
        end_lines = []

        for line in self._d.split_newline(text):
            wrapped_line = wrap_function(line)

            if wrapped_line:
                start_lines.append(len(wrapped) + 1)  # add 1 line for next wrapped_line were added
                wrapped.extend(wrapped_line)

                nline = len(wrapped)

                if has_max_lines and nline <= max_lines:
                    # only added if it has the max_lines attribute and the current line is no more than max_lines
                    end_lines.append(nline)
                elif not has_max_lines:
                    # if not set
                    end_lines.append(nline)

            elif empty_lines:
                wrapped.append('')  # adding an empty string (usually occurs when encountering an empty line)

                nline = len(wrapped)

                start_lines.append(nline)
                end_lines.append(nline)

            if has_max_lines and len(wrapped) > max_lines:
                # cut off the excess part of the wrapper and also add a placeholder to indicate that the wrapper has
                # been cut off.
                current_part = ''

                for part in wrapped[max_lines - 1]:
                    if length_function(current_part + part + placeholder) > width:
                        break
                    current_part += part

                wrapped[max_lines - 1] = current_part + placeholder
                wrapped = wrapped[:max_lines]

                # add max_lines line to end_lines
                end_lines.append(max_lines)
                break

        return {
            'wrapped': wrapped,
            'start_lines': start_lines,
            'end_lines': end_lines
        } if return_details else wrapped

    def align(self, text, return_details=False):
        width = self._d.width
        line_padding = self._d.line_padding
        alignment = self._d.alignment
        justify = self._d.align_justify
        minimum_width = self._d.minimum_width
        size_function = self._d.size_function

        if size_function is None:
            # if using length_function (align function need to use size_function)
            raise TypeError("size_function must be a size")

        wrapped_info = self.wrap(text, True)

        wrapped = wrapped_info['wrapped']
        end_lines = set(wrapped_info['end_lines'])  # convert to set for faster lookup

        aligned = []
        offset_y = 0

        lines_size = [size_function(line) for line in wrapped]
        use_width = (max(size[0] for size in lines_size) if lines_size else 0) if minimum_width else width

        if alignment in {'left', 'center', 'right'}:
            for i, line in enumerate(wrapped):
                width_line, height_line = lines_size[i]
                justify(aligned, line, use_width, width_line, offset_y)
                offset_y += height_line + line_padding

        else:
            # alignment='fill-...'

            split_space = self._d.split_space
            justified_last_line = not self._d.justify_last_line
            lines_word = [self._split(line, split_space) for line in wrapped]

            if minimum_width and any(len(line) > 1 and not (justified_last_line and i in end_lines)
                                     for i, line in enumerate(lines_word, start=1)):
                use_width = width if wrapped else 0

            for i, line in enumerate(wrapped):
                width_line, height_line = lines_size[i]

                if justified_last_line and i + 1 in end_lines:
                    # end lines
                    justify(aligned, line, use_width, width_line, offset_y)

                else:
                    words = lines_word[i]
                    total_words = len(words)

                    if total_words > 1:
                        all_word_width = [size_function(word)[0] for word in words]
                        extra_space = width - sum(all_word_width)
                        space_between_words = extra_space / (total_words - 1)
                        offset_x = 0

                        for j, word in enumerate(words):
                            aligned.append((offset_x, offset_y, word))
                            offset_x += all_word_width[j] + space_between_words
                    else:
                        # only 1 word in the line
                        justify(aligned, line, use_width, width_line, offset_y)

                offset_y += height_line + line_padding

        return {
            'aligned': aligned,
            'wrapped': wrapped,
            'start_lines': wrapped_info['start_lines'],
            'end_lines': wrapped_info['end_lines'],
            'size': (use_width, offset_y - line_padding)
        } if return_details else aligned

    def fillstr(self, text):
        # The way this function works is almost the same as align function

        width = self._d.width
        line_padding = self._d.line_padding
        alignment = self._d.alignment
        space_character = self._d.space_character
        newline_character = self._d.newline_character
        justify = self._d.fillstr_justify
        minimum_width = self._d.minimum_width
        length_function = self._d.length_function

        wrapped_info = self.wrap(text, True)

        wrapped = wrapped_info['wrapped']
        end_lines = set(wrapped_info['end_lines'])

        justified = []

        lines_width = [length_function(line) for line in wrapped]
        use_width = (max(lines_width) if lines_width else 0) if minimum_width else width
        add_padding = line_padding > 0

        if alignment in {'left', 'center', 'right'}:
            spaces = space_character * use_width
            fill_line_padding = newline_character.join(spaces for _ in range(line_padding))

            for i, line in enumerate(wrapped):
                justify(justified, line, use_width, lines_width[i], space_character)
                if add_padding:
                    justified.append(fill_line_padding)

        else:
            split_space = self._d.split_space
            justified_last_line = not self._d.justify_last_line
            lines_word = [self._split(line, split_space) for line in wrapped]

            if minimum_width and any(len(line) > 1 and not (justified_last_line and i in end_lines)
                                     for i, line in enumerate(lines_word, start=1)):
                use_width = width if wrapped else 0

            spaces = space_character * use_width
            fill_line_padding = newline_character.join(spaces for _ in range(line_padding))

            for i, line in enumerate(wrapped):

                if justified_last_line and i + 1 in end_lines:
                    justify(justified, line, use_width, lines_width[i], space_character)

                else:
                    words = lines_word[i]
                    total_words = len(words)

                    if total_words > 1:
                        extra_space = width - sum(length_function(w) for w in words)
                        space_between_words = extra_space // (total_words - 1)
                        extra_padding = extra_space % (total_words - 1)
                        justified_line = ''

                        for i, word in enumerate(words):
                            justified_line += word
                            if i < total_words - 1:
                                justified_line += space_character * (space_between_words +
                                                                     (1 if i < extra_padding else 0))

                        justified.append(justified_line if justified_line else spaces)
                    else:
                        justify(justified, line, use_width, lines_width[i], space_character)

                if add_padding:
                    justified.append(fill_line_padding)

        if add_padding and justified:
            # remove the last padding line
            justified.pop()

        return newline_character.join(justified)

    def shorten(self, text):
        # _one_line parameter to change the wrap behavior of max_lines as if set to 1 line max. If this is set via
        # `self.max_lines = 1` it can cause "race condition"
        wrapped = self.wrap(text, _one_line=True)
        return wrapped[0] if wrapped else ''

def wrap(text, width=70, mode='word', placeholder='...', space_character=' ', word_separator=None,
         newline_separator=None, max_lines=None, empty_lines=True, excess_word_separator=False, break_on_hyphens=True,
         return_details=False, size_function=None):
    return TextWrapper(width=width, mode=mode, placeholder=placeholder, space_character=space_character,
                       word_separator=word_separator, newline_separator=newline_separator, max_lines=max_lines,
                       empty_lines=empty_lines, excess_word_separator=excess_word_separator,
                       break_on_hyphens=break_on_hyphens, size_function=size_function).wrap(text, return_details)

def align(text, width=70, line_padding=0, mode='word', alignment='left', placeholder='...', space_character=' ',
          newline_character='\n', word_separator=None, newline_separator=None, max_lines=None, empty_lines=True,
          minimum_width=True, excess_word_separator=False, justify_last_line=False, break_on_hyphens=True,
          return_details=False, size_function=None):
    return TextWrapper(width=width, line_padding=line_padding, mode=mode, alignment=alignment, placeholder=placeholder,
                       space_character=space_character, newline_character=newline_character,
                       word_separator=word_separator, newline_separator=newline_separator, max_lines=max_lines,
                       empty_lines=empty_lines, minimum_width=minimum_width,
                       excess_word_separator=excess_word_separator, justify_last_line=justify_last_line,
                       break_on_hyphens=break_on_hyphens, size_function=size_function).align(text, return_details)

def fillstr(text, width=70, line_padding=0, mode='word', alignment='left', placeholder='...', space_character=' ',
            newline_character='\n', word_separator=None, newline_separator=None, max_lines=None, empty_lines=True,
            minimum_width=True, excess_word_separator=False, justify_last_line=False, break_on_hyphens=True,
            size_function=None):
    return TextWrapper(width=width, line_padding=line_padding, mode=mode, alignment=alignment, placeholder=placeholder,
                       space_character=space_character, newline_character=newline_character,
                       word_separator=word_separator, newline_separator=newline_separator, max_lines=max_lines,
                       empty_lines=empty_lines, minimum_width=minimum_width,
                       excess_word_separator=excess_word_separator, justify_last_line=justify_last_line,
                       break_on_hyphens=break_on_hyphens, size_function=size_function).fillstr(text)

def shorten(text, width=70, mode='word', placeholder='...', space_character=' ', word_separator=None,
            newline_separator=None, excess_word_separator=True, break_on_hyphens=True, size_function=None):
    return TextWrapper(width=width, mode=mode, placeholder=placeholder, space_character=space_character,
                       word_separator=word_separator, newline_separator=newline_separator,
                       excess_word_separator=excess_word_separator, break_on_hyphens=break_on_hyphens,
                       size_function=size_function).shorten(text)