"""
Package setup.

Set me up with `python setup.py bdist_wheel --universal`
"""
from setuptools import setup, Extension
setup(
    name='ascii-train',
    version='0.0.2',
    description='Print an ascii train!',
    author='Noah Pendleton',
    author_email='2538614+noahp@users.noreply.github.com',
    url='https://github.com/noahp/ascii-train',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    py_modules=['ascii_train'],

    entry_points={
        'console_scripts': [
            'ascii-train = ascii_train:main'
        ]
    },

    # For scripts, this corrects shebang replacement, from:
    #  https://github.com/pybuilder/pybuilder/issues/168
    options={'build_scripts': {'executable': '/usr/bin/env python'}},
)
