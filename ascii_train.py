#!/usr/bin/env python
"""
Print an ascii train!

Wraps + centers + truncates text passed in the first argument or stdin into the steam cloud.
"""
from __future__ import print_function
import sys
import textwrap

# Train credit to https://www.asciiart.eu/vehicles/trains !
ASCII_TRAIN_FORMAT = """                 _-====-__-======-__-========-_____-============-__
               _( {:^47} _)
            OO( {:^49} )_
           0  (_ {:^49} _)
         o0     (_ {:^46} _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (BNSF 1995| |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################"""


def train(text_input=''):
    """Format an ascii train using the optional parameter:text_input as text"""
    # wrap text to lines of 47,49,49,46
    # first get number of lines
    linecounts = [(49, 1), (49+49, 2), (47+49+49, 3), (47+49+49+46, 4)]
    number_of_lines = 4  # default to max
    for linecount in linecounts:
        if len(text_input) <= linecount[0]:
            number_of_lines = linecount[1]
            break

    linecount_wraps = {1: (0, 49,), 2: (0, 49, 49), 3: (
        47, 49, 49), 4: (47, 49, 49, 46)}
    outlines = ['']*4
    for index, linewidth in enumerate(linecount_wraps[number_of_lines]):
        if not linewidth:
            continue
        text_wrapped = textwrap.wrap(text_input, linewidth)
        if text_wrapped:
            outlines[index] = text_wrapped[0][:linewidth]
        if len(text_wrapped) > 2:
            text_input = ' '.join(text_wrapped[1:])

    return ASCII_TRAIN_FORMAT.format(*outlines)


def test_train():
    """Test the train"""
    assert train() == ASCII_TRAIN_FORMAT.format(*(('',)*4))

    LOREM_TRAIN = """                 _-====-__-======-__-========-_____-============-__
               _(     Lorem ipsum dolor sit amet, consectetur     _)
            OO( adipiscing elit, sed do eiusmod tempor incididunt )_
           0  (_   ut labore et dolore magna aliqua. Ut enim ad    _)
         o0     (_    minim veniam, quis nostrud exercitation     _)
        o         \'=-___-===-_____-========-___________-===-dwb-=\'
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (BNSF 1995| |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################"""
    assert train("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                 "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
                 "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                 "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
                 "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                 "culpa qui officia deserunt mollit anim id est laborum.") == LOREM_TRAIN


def test_main():
    """Test main?"""
    main()


def main():
    """Print the ascii train"""
    text = ''
    if len(sys.argv) > 1:
        text = sys.argv[1]
    elif not sys.stdin.isatty():
        text = sys.stdin.read()

    print(train(text))


if __name__ == '__main__':
    main()
