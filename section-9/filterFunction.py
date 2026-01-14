"""What is filter() function in Python?
👉 filter() is used to select only the elements you want from an iterable.
It filters out unwanted values.

“Keep only what matches the condition.”
"""

letters = ['a', 'B', 'c', 'D']

result = filter(lambda x: x.isupper(), letters)

print(list(result))





