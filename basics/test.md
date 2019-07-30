# assert

if a python file is run with the -O flag, assertions will not be evaluated

```
assert user.is_admin, 'Only admins can do bad things!'
```


# doctests

```
def add(x, y):
  """
  >>> add(2, 3)
  5
  >>> add(100, 200)
  300
  """
  return x + y
```
python3 -m  doctest -v file_name.py

# unittest
test each method in details and show comments of each method
python file_name.py -v

setUp and tearDown
```
class testClass(unittest.TestCase):
```
