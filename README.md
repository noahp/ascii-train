# ascii-train
Prints out an ascii train, optionally with a text string passed as first arg or via stdin.

```bash
➜ ./ascii-train "choo choo\!"
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

➜ echo "all aboard\!" | ./ascii-train
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
