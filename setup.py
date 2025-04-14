from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='txtwrap',
    version='3.0.1',
    description='A tool for wrapping and filling text.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='azzammuhyala',
    author_email='azzammuhyala@gmail.com',
    url='https://github.com/azzammuhyala/txtwrap',
    project_urls={
        'Source': 'https://github.com/azzammuhyala/txtwrap',
        'Bug Tracker': 'https://github.com/azzammuhyala/txtwrap/issues'
    },
    license='MIT',
    python_requires='>=3.0',
    packages=find_packages(),
    include_package_data=True,
    keywords=['wrap', 'wrapper', 'wrapping', 'wrapped', 'text wrap', 'text wrapper', 'text wrapping', 'text wrapped'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters'
    ]
)