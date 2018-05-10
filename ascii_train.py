#!/usr/bin/env python
"""
Print an ascii train!

Wraps + centers + truncates text passed in the first argument or stdin into the steam cloud.
"""
from __future__ import print_function
import sys
import textwrap

# Train credit to https://www.asciiart.eu/vehicles/trains !
ASCII_TRAIN_FORMAT = """               _-====-__-======-__-========-_____-============-_
              ( {three:^47} ){bonus_lines}
            OO( {one:^47} )_
           0  (_ {two:^47} _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (BNSF 1995| |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################"""
ASCII_TRAIN_BONUS_SMOKE_LINE_FORMAT = """
              ( {text:^47} )"""


def train(text_input=''):
    """Format an ascii train using the optional parameter:text_input as text"""
    # wrap text to lines of 47
    smoketext_lines = textwrap.wrap(text_input, 47)

    bonus_lines = ''
    if len(smoketext_lines) > 3:
        bonus_lines = ''.join([ASCII_TRAIN_BONUS_SMOKE_LINE_FORMAT.format(
            text=line) for line in smoketext_lines[2:-2]])

    outlines = {
        'three': smoketext_lines[0] if len(smoketext_lines) > 2 else '',
        'one': smoketext_lines[-2] if len(smoketext_lines) > 1 else smoketext_lines[0] if len(smoketext_lines) > 0 else '',
        'two': smoketext_lines[-1] if len(smoketext_lines) > 1 else '',
        'bonus_lines': bonus_lines,
    }

    return ASCII_TRAIN_FORMAT.format(**outlines)


def test_train():
    """Test the train"""
    assert train() == ASCII_TRAIN_FORMAT.format(
        three='', bonus_lines='', one='', two='')

    LOREM_TRAIN = """               _-====-__-======-__-========-_____-============-_
              (     Lorem ipsum dolor sit amet, consectetur     )
              ( incididunt ut labore et dolore magna aliqua. Ut )
              ( enim ad minim veniam, quis nostrud exercitation )
              (  ullamco laboris nisi ut aliquip ex ea commodo  )
              (       consequat. Duis aute irure dolor in       )
              (  reprehenderit in voluptate velit esse cillum   )
              ( dolore eu fugiat nulla pariatur. Excepteur sint )
              ( occaecat cupidatat non proident, sunt in culpa  )
            OO(     qui officia deserunt mollit anim id est     )_
           0  (_                    laborum.                     _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
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
