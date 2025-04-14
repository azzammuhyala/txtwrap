import re

pdict = type('pdict', (dict,), {
    '__repr__': lambda self : '{}({})'.format(type(self).__name__, dict.__repr__(self)),
    '__getattr__': lambda self, key: self.get(key, None),
    '__setattr__': dict.__setitem__,
    '__delattr__': dict.__delitem__
})

def align_left(aligned, text, width, text_width, offset_y):
    aligned.append((0, offset_y, text))

def align_center(aligned, text, width, text_width, offset_y):
    aligned.append(((width - text_width) / 2, offset_y, text))

def align_right(aligned, text, width, text_width, offset_y):
    aligned.append((width - text_width, offset_y, text))

def fillstr_left(justified_lines, text, width, text_width, fillchar):
    justified_lines.append(text + fillchar * (width - text_width))

def fillstr_center(justified_lines, text, width, text_width, fillchar):
    extra_space = width - text_width
    left_space = extra_space // 2
    justified_lines.append(fillchar * left_space + text + fillchar * (extra_space - left_space))

def fillstr_right(justified_lines, text, width, text_width, fillchar):
    justified_lines.append(fillchar * (width - text_width) + text)

hyphenate_parrent = r'''
(?<=-)      # positive lookbehind: make sure there is a '-' before the current position
(?=(?!-).)  # positive lookahead: make sure the character after is NOT '-' (avoid '--'), but still have one character
'''
split_hyphenated = re.compile(hyphenate_parrent, re.VERBOSE).split