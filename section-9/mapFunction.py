"""What is map() function in Python?
👉 map() is used to apply the same operation to every item in an iterable.
It transforms data."""

nums = [1, 2, 3, 4]
def square(n):
    return n * n
result = map(square, nums)
print(list(result))


# example 2

names = ["ram", "shyam", "mohan"]
result = map(str.upper, names)
print(list(result))





