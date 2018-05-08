[![PyPI version](https://img.shields.io/pypi/v/ascii-train.svg?longCache=true&style=for-the-badge)](https://pypi.org/project/ascii-train/)

# ascii-train
Prints out an ascii train, optionally with a text string passed as first arg or via stdin.

# Installing
Now deployed to pypi, install with:
```bash
pip install ascii-train
```

# Usage
# cli
```bash
➜ ascii-train "choo choo\!"
                 _-====-__-======-__-========-_____-============-__
               _(                                                 _)
            OO(                    choo choo!                     )_
           0  (_                                                   _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (BNSF 1995| |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################

➜ echo "all aboard\!" | ascii-train
                 _-====-__-======-__-========-_____-============-__
               _(                                                 _)
            OO(                    all aboard!                    )_
           0  (_                                                   _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (BNSF 1995| |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################
```

## Embedding
```python
import ascii_train

print(ascii_train.train("No brakes!"))
```
Outputs:
```bash
# Run the above as cli passed to interpreter
➜ python -c 'import ascii_train; print(ascii_train.train("No brakes!"))'
                 _-====-__-======-__-========-_____-============-__
               _(                                                 _)
            OO(                    No brakes!                     )_
           0  (_                                                   _)
         o0     (_                                                _)
        o         '=-___-===-_____-========-___________-===-dwb-='
      .o                                _________
     . ______          ______________  |         |      _____
   _()_||__|| ________ |            |  |_________|   __||___||__
  (BNSF 1995| |      | |            | __Y______00_| |_         _|
 /-OO----OO""="OO--OO"="OO--------OO"="OO-------OO"="OO-------OO"=P
#####################################################################
```

# Tests
Yeah there are tests WHYNOT!

Prereqs are installed via `pip install -e '.[test]'`.

To run them:
```bash
pytest ascii_train.py -vv --cov=./ --cov-branch --cov-report html:pytest_output
```
View results by loading `pytest_output/index.html` in a browser.
