print(10 > 9)
print(10 == 9)
print(10 < 9)
# comparison expression is evaluated and returns a boolean

# Prints message based on whether condition is true or false
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# bool() function evaluates any value given
print(bool("Hello"))
print(bool(15))

# evaluate variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# Functions can return boolean
def myFunction():
    return True


print(myFunction())


# Functions can execute code based on the boolean answer of a function
def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

# Py has many built-in functions that return boolean
# isinstance checks if obj is of a certain data type
x = 200
print(isinstance(x, int))
