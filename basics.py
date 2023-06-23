print("Hello, World!")

# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(type(x))
print(y)

# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.
x = "Sally"
print(x)

# If you want to specify the data type of variables,
# this can be done with casting.
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of variables with the type() function.
print(x, y, z)

# Global variables can be used by everyone, inside and outside functions:
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# Local variables will be used first and leave the global unchanged
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)  # fantastic


myfunc()

print("Python is " + x)


# You can declare global variables inside a function with the global keyword
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

# You can specify data types with 'casting'
x = int(1)  # x will be 1
y = float(3)  # y will be 3.0
z = str("4")  # z will be '4'

# You can assign a multiline string with three quotes or three single quotes
a = '''Lorem ipsum dolor
sit amet consectetur adipiscing elit
ut labore et'''
print(a)

# Strings are arrays and can be accessed as such
for x in "banana":  # will loop through the letters
    print(x)

# Slicing string arrays
b = "Hello, World!"
print(b[2:5])  # gets the characters from index 2 to 5(not included!)

# use 'negative' to start from the end of string
c = "Howdy, Folks!"
print(c[-5:-2])

# concatenate
a = "Hello"
b = "World"
c = a + b
print(c)
