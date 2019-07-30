class Person:
    tol_num_property = 0

    def __init__(self, name, age):
        self._name = name
        Person.tol_num_property += 1
        self.age = age
        Person.tol_num_property += 1

    def __repr__(self):
        return self._name

    @classmethod
    def get_num_property(cls):
        return cls.tol_num_property

    def hobby(self):
        self.hobby = 'accordian'
        Person.tol_num_property += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Men(Person):
    def __init__(self, name, is_married):
        super().__init__(name, age=20)  # same as Person.__init__(self, name, age=20)
        self.is_married = is_married


if __name__ == '__main__':
    marks = Person('mark', 23)
    marks.hobby()
    print(marks)
    print(marks.name)
    marks.name = 'tom'
    print(marks.name)
    print(marks.__dict__)  # print all instance atrributes as dict
    print(Person.get_num_property())
