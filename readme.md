#### Tested in
Python 2.7

#### Requires numpy module
Run `pip install numpy` if needed.

#### Usage and output
Run the script with 4 arguments.  
1st arg: Represents cols of the board  
2nd arg: Represents rows of the board  
3rd arg: Starting x location  
4th arg: Starting y location

`python knights.py 3 4 0 0`:
```
  0  3  2
  3  4  1
  2  1  4
  5  2  3
```

`-1` is printed if the position is impossible to get to.

`python knights.py 3 3 0 2`:
```
  2  1  4
  3 -1  1
  0  3  2
```

#### Running the Test
Test only checks for getting legal moves  
Requires: unittest module

Run `python test.py`