import math
from typing import Union

# Data types and Variables
students_count = 1000
rating = 4.99
is_published = False
course_name = """
Multiple
Lines
"""

x, y = 1, 2
x = y = 1

print(type(students_count))
print(type(1.1))
print(type(False))
print(type(""))

# Type annotation
# use mypy linter
age: int = 20
age = "Python"
print(age)

# Mutable and Immutable Types
# immutable object cannot be changed after is created
# int, float, bool, str, tuple - immutable
x = 1
print(id(x))
x += 1
print(id(x))
# list, dictionary, set - mutable
x = [1, 2, 3]
print(id(x))
x.append(4)
print(id(x))

# Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[:])
print(id(course))
print(id(course[0]))

# Escape Sequences: \" \' \\ \n
message = "Python \"Programming"
print(message)

# Formatted Strings
first = "Mosh"
last = "Hamedani"
# full = first + " " + last
full = f"{first} {last}"
print(full)
full = f"{len(first)} {2+2}"
print(full)

# Useful String Methods
course = " Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("P", "-"))
print("Programming" in course)
print("Programming" not in course)

# Numbers
x = 10
x = 0b10
print(bin(x))
x = 0x12c
print(hex(x))
x = 1 + 2j
print(x)

x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3
x = 10 // 3
x = 10 % 3
x = 10 ** 3
print(x)
x += 1

PI = -3.14  # uppercase letters for constants
print(round(PI))
print(abs(PI))
print(math.floor(PI))
print(math.ceil(PI))

# Type Conversion
# x = input("x: ")
print(int(x))
print(float(x))
print(bool(x))

# Falsy values: "", 0, [], None

# Conditional Statements
age = 22
if age >= 18:
    print("Adult")
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("All done")

# Walrus Operator
if (n := len(course)) > 10:
    print(f"Too long {n} characters")

# Logical Operators
name = " "
if not name.strip():
    print("Name is empty")

age = 20
if age >= 18 and age < 65:  # if 18 <= age < 65:
    print("Eligible")
else:
    print("Not eligible")

# Ternary Operator
message = "Eligible" if age >= 18 else "Not eligible"

# Loops
for x in "Python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(0, 1000000, 2):
    print(x)

# List vs Range objects
print(range(5))
print(type(range(5)))
print([1, 2, 3, 4, 5])

# For..Else
names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("break was not reached")

guess = 5
answer = 5
while answer != guess:
    guess = int(input("Guess: "))



# Functions
def increment(number: int, by: int = 1) -> tuple[int, int] | None:
    return number, number + by


print(increment(number=2, by=3))  # Keyword arguments
print(increment(2))


# Arguments - xargs
def multiply(*lst):
    total = 1
    for number in lst:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))


# Arguments - xxargs
def save_user(**user):
    print(user["id"])

    if "option" in user:
        # do smth
        pass 


save_user(option=5)


# Scope
# in Python we do not have block level scope
def greet():
    if True:
        message = "a"
    print(message)


# It is a good practice not to modify a global variable from a function
# a new local variable is created inside the function
message = "a"


def greet2():
    message = "b"
    print(message)


greet2()
print(message)


# Global keyword -> Avoid it!
message = "a"


def greet3():
    global message
    message = "b"
    print(message)


greet3()
print(message)
