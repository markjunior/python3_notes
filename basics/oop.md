# class and instance
class: a blueprint for objects  
instance: objects that are constructed from a class


self refers to the current class instance

# _ name, __ name, __ name __
_ name: private
__ name: name mangling

```
self.__name = 'xxxx ' # instance._classname__name = 'xxx'
```


# class method, class attribute

```
@classmethod
def method(cls):
  pass
```


# Encapsulation
encapsulation is the process of designing a programmatic class using public and private methods and attributes to implement abstractions.


# property
```
@property
def age(self):
  pass

@age.setter
def age(self, value):
  self._age = value
```


# Inheritance
Can be seen by
```
classname.__mro__
classname.mro()
help(classname)
```


# Polymorphism
1. The same class method works in a similar way for different classes
```
raise NotImplementedError('subclass should implement this method')
```
2. The same operation works for different kinds of objects
```
8+2 = 10
‘8’ + ‘2’ = ’82‘
```
