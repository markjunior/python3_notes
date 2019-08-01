function input
order: parameters, \*args, default_parameters, \*\*kwargs

#lambda
only used once
no name
```
fn_add = lambda a,b: a + b
fn_add(a, b) #return a + b
fn_add.__name__ # <lambda>
```

#map
```
map(fn, list) # return [fn(i) for i in list]
return an iterator, which can only be used once
```

#filter

```
filter(fn_return_bool, list)
```


#sorted
reverse
key=len #fn for sorting
```
sorted(users, key=lambda user: user['name'])
```


#zip
```
nums = [[2,3],[1,21,3], [23,1,3]]
list(zip(*nums)) #[[2,1,23], [3,21,1]]
```

# == vs is 
