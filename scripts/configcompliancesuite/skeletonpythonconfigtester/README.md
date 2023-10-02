# config file validity tester
## Sample python script for checking compliance of config files

### Sample Usage
`$ python3 init.py`

On failure, returns the number of checks failed.

`$ echo $?`

## Correct Test Output
FooOption yes

PASSED:  FooOption yes

BarOption no

FAILED:  BarOption no

MISSING:  XyzzyOption
Checks passed  1 / 4
Some checks failed` 
