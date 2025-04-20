import txtwrap

def line():
    print('=' * 70)

# methods test
print('TxTWrap test in Version:', txtwrap.__version__)
line()
wrapper = txtwrap.TextWrapper()
print('Origin:', wrapper)
print('Copy:  ', wrapper.copy())
print('Repr:  ', repr(wrapper))
print('_d:    ', wrapper._d)
line()
print(txtwrap.wrap(txtwrap.LOREM_IPSUM_PARAGRAPHS))
line()
print(txtwrap.align(txtwrap.LOREM_IPSUM_PARAGRAPHS))
line()
print(txtwrap.fillstr(txtwrap.LOREM_IPSUM_PARAGRAPHS))
line()
print(txtwrap.shorten(txtwrap.LOREM_IPSUM_PARAGRAPHS))

# error test
line()
print(txtwrap.wrap(txtwrap.LOREM_IPSUM_SENTENCES, size_function=lambda s : 4 if s == 'test' else -1))