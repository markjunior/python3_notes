#Iterator and Iterable

'hello' is an iterable, but it is not an iterator
```
iterator = iter('hello') # is an iterator
next(iterator)
next(iterator)
next(iterator)
```


# Generators

all generators are iterators, but not all iterators are generators
generator function use the yield keyword

```
def count_up_to(max):
  count = 1
  while count <= max:
    yield count
    count += 1

counter = count_up_to(10)
next(counter)
list(counter)
import sys
sys.getsizeof(counter)
sys.getsizeof(list(counter))
```
