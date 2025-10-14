from timeit import timeit
import logging

# numbers = [1, 2]
# print(numbers[3])  # IndexError exception
# build in exceptions vs custom exceptions ?

# --- Handling Exceptions ---
try:
     with open("app.py") as file:
        age = int(input("Age: "))
        xfactor = 10 / age
except (ValueError, ZeroDivisionError, FileNotFoundError) as ex:
    # logging
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
# except ZeroDivisionError:
#     print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    print('Finally')
print("Execution continues.")


# --- Cost of raising Exceptions ---
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))


# custom exceptions
class MyCustomError(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "This error is casued by the missing params"):
        self.message = message
        super().__init__(self.message)
