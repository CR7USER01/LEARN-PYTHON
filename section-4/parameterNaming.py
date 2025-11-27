# code 1
class Movie:
    def __init__(self, name, year):
        self.name = name # here name is a property of self not a variable
        self.year = year

matrix = Movie('The Matrix', 1994)

print(matrix.name)






