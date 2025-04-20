import re

pdict = type('pdict', (dict,), {
    '__repr__': lambda self : '{0}({1})'.format(type(self).__name__, dict.__repr__(self)),
    '__getattr__': lambda self, key: self.get(key, None),
    '__setattr__': dict.__setitem__,
    '__delattr__': dict.__delitem__
})

unknown = type('unknown', (), {
    '__repr__': lambda self : '<unknown>',
    '__str__': lambda self : '<unknown>',
    '__bool__': lambda self : False
})()

def align_left(aligned, text, width, text_width, offset_y):
    aligned.append((0, offset_y, text))

def align_center(aligned, text, width, text_width, offset_y):
    aligned.append(((width - text_width) / 2, offset_y, text))

def align_right(aligned, text, width, text_width, offset_y):
    aligned.append((width - text_width, offset_y, text))

def fillstr_left(justified, text, width, text_width, fillchar):
    justified.append(text + fillchar * (width - text_width))

def fillstr_center(justified, text, width, text_width, fillchar):
    extra_space = width - text_width
    left_space = extra_space // 2
    justified.append(fillchar * left_space + text + fillchar * (extra_space - left_space))

def fillstr_right(justified, text, width, text_width, fillchar):
    justified.append(fillchar * (width - text_width) + text)

def validate_size_function(func, test):
    result = func(test)

    if isinstance(result, tuple):

        def wrapper(string):
            result = func(string)
            if not isinstance(result, tuple): 
                raise TypeError("size_function must be returned a tuple for size")
            if len(result) != 2:
                raise ValueError("size_function must be returned a tuple of length 2")
            width, height = result
            if not isinstance(width, (int, float)):
                raise TypeError("size_function returned width must be a tuple of two integers or floats")
            if not isinstance(height, (int, float)):
                raise TypeError("size_function returned height must be a tuple of two integers or floats")
            if width < 0:
                raise ValueError("size_function returned width must be equal to or greater than 0")
            if height < 0:
                raise ValueError("size_function returned height must be equal to or greater than 0")
            return result

        return wrapper, lambda string : wrapper(string)[0]

    elif isinstance(result, (int, float)):

        def wrapper(string):
            result = func(string)
            if not isinstance(result, (int, float)):
                raise TypeError("size_function (length) must be returned a integers or floats for width")
            if result < 0:
                raise ValueError("size_function (length) must be equal to or greater than 0")
            return result    

        return None, wrapper

    raise TypeError("size_function must be returned a tuple for size or a single value for width (length)")

hyphenate_pattern = r'''
(?<=-)      # positive lookbehind: make sure there is a '-' before the current position
(?=(?!-).)  # positive lookahead: make sure the character after is NOT '-' (avoid '--'), but still have one character
'''
split_hyphenated = re.compile(hyphenate_pattern, re.VERBOSE).split