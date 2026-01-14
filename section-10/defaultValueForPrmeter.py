"""Default values for parameters in Python (very simple)
A default parameter value means:
If you don’t give a value when calling a function, Python uses the default value."""

def greet(name="Guest"):
    print("Hello", name)

greet("Jitu")   # value given
greet()         # no value given

#Output
#Hello Jitu
#Hello Guest

