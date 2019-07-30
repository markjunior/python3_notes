# Errors

SyntaxError
NameError: the variable is not defined.
TypeError: operation or function is applied to the wrong type
IndexError: access index out of defined range
ValueError: built-in operation or function receives an argument that has the right type but an inappropriate value
KeyError:  the dict does not have a specific key
AttributeError: the variable does not have attribute

# codes
```
try:
  raise ValueError('THIS IS THE VALUE ERROR')
except ValueError as e:
  print(e) #  should print 'THIS IS THE VALUE ERROR'
else:
  print('There is no Value Error')
finally:
  print('run no matter what')
print('codes going on running')
```


# debugging
import pdb
pdb.set_trace()
(pdb) l
(pdb) n
(pdb) c
(pdb) p # (print)
