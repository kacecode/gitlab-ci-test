import sys

from main import square

assert square(2) is 4
assert square(3) is 9
assert square(-1) is 1

if "--fail" in sys.argv:
    assert square(10) is 1
