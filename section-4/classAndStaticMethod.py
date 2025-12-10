"""class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []


    def average(self):
        return sum(self.marks) / len(self.marks)
    

rolf = Student('Rolf', 'MIT')
jitu = Student('jitu', 'PMEC')
               
rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())

jitu.marks.append(100)
jitu.marks.append(99)
print(jitu.average())

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I dont \' take parameters.')

another_object = Bar()
another_object.hi()"""

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)


new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"    # Euro symbol

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"

