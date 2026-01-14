#Example: List vs Generator
#Using a list
"""def numbers_list():
    return [1, 2, 3, 4]


#All values are created and stored together.

#Using a generator
def numbers_gen():
    yield 1
    yield 2
    yield 3
    yield 4"""
    
    #using loops
def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)