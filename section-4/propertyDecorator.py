

"""What is a Property Decorator in Python?

A property decorator (@property) is used inside a class to make a method behave like a variable.

It is mainly used for getting, setting, and controlling access to class attributes."""

class Dog:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

d = Dog(5)
print(d.age)     # no (), looks like a variable but calls a method


   #@property, @setter, @deleter
   #Real-life examples (salary, marks, bank account)
   #Why we don’t access private variables directly