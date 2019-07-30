from functools import wraps

def decoratorsa(clss):
    rec = {}
    @wraps(clss)
    def wrapper(name):
        if name not in rec:
            rec[name] = clss(name)
        return rec[name]
    return wrapper

@decoratorsa
class ClassDeco:
    def __init__(self, name):
        self.name = name


a = ClassDeco('mark')
b = ClassDeco('mark')
print(a is b)
