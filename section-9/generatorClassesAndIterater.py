"""__init__ = SETUP
Meaning: “Remember where to start and where to stop”
Like telling a boy:
Start counting from 1 and stop at 3
Nothing more.
2️⃣ __next__ = GIVE NEXT NUMBER
Meaning: “Give me the next number”
First call → gives 1
Second call → gives 2
Third call → gives 3
Fourth call → says NO MORE
3️⃣ StopIteration = STOP SIGNAL
Meaning: “Numbers finished, stop asking”
Like saying:
Done. Go away."""

class EvenOdd:
    def __init__(self, limit):
        self.num = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.limit:
            raise StopIteration
        else:
            if self.num % 2 == 0:
                result = "Even"
            else:
                result = "Odd"

            value = (self.num, result)
            self.num += 1
            return value
for n, t in EvenOdd(5):
    print(n, "is", t)
