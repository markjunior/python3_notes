```
string.upper()
```



list addition
```
ori_list = [1,2]
ori_list.append(3)
ori_list.extend([3,4,5,6])
ori_list.insert(-1, 'insert_value') # insert before the last one of the list
```

list removal
```
ori_list = [1,2,1]
ori_list.clear()
ori_list.pop(0)
ori_list.remove(1) # remove the first element
```

list index
```
ori_list = [1, 2, 3, 4, 'adam', 'adam']
ori_list.index(0, start_index=1, end_index=3)
ori_list.count('adam')
ori_list.reverse()
ori_list.sort()
' '.join() # string method
```

slicing
```
ori_list = [1, 2, 3, 4, 5, 6]
ori_list[2::-1] # = [3, 2, 1]
```

dict
```
{}. fromkeys(['name', 'score', 'email'], 'unknown')
{}. fromkeys('name', 'unknown')
{}. fromkeys(range(10), 'unknown')
dict().get(no_key) # return None
dict().get(no_key, replace_value_if_None) # return replace_value_if_None
dict().pop(key)
dict().update(dict()) # add new key, value and update value with same key
{(k.upper() if k is 'color' else k): v.upper() for k,v in instructor.items()}
```

tuple
- tuple object does not allow assignment
```
tuple([1,2,1,1]).count(1) = 3
tuple([1,2,1,1]).index(1) = 0 # the first element
```

set
```
remove (show error if no key) vs discard (no error)
```

string
```
string_sentance.replace(' ', '')
string_sentance.strip()
