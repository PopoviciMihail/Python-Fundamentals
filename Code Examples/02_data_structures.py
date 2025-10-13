from array import array
from collections import deque
from sys import getsizeof

# --- Lists ---
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(len(chars))

letters = ["a", "b", "c", ""]
letters[0] = "A"
print(letters[0:3])
print(letters[:])  # copy of the original list

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

# List Unpacking
numbers = [1, 2, 3, 4, 4, 4, 9]
first = numbers[0]
second = numbers[1]
third = numbers[2]

first, second, third, *other = numbers  # List unpacking and packing (*)
print(first)
print(other)

first, *other, last = numbers
print(other)

# Loop over lists
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)


# Add
letters.append("d")
letters.insert(0, "-")

# Remove
letters.pop()
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()

# Find
letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

# Sort
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))  # new sorted list
print(numbers)

# Lambda function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


# items.sort(key=sort_item)
items.sort(key=lambda item: item[1])

# Map Function
prices = list(map(lambda item: item[1], items))
# Filter Function
filtered = list(filter(lambda item: item[1] >= 10, items))

# List Comprehensions
# [expression for item in items]
prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]

# examples
y = [el for el in list(range(20)) if el % 2 == 0]
y = [el if el % 2 == 0 else None for el in list(range(20))]

# Zip Function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))

# --- Stack (LIFO) ---
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
if not browsing_session:
    print("Empty")

# --- Queues (FIFO) ---
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")

# --- Tuples ---
point = (1, 2)
point = 1, 2
point = (1,)
point = ()
print(type(point))
point = (1, 2) + (3, 4)
point = (1, 2) * 3
point = tuple([1, 2])
print(point[0])

point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")

# point[0] = 10 # cannot do this

# Swapping variables
x = 10
y = 11
x, y = y, x

# --- Arrays ---
# -> dealing with large sequence of numbers
# -> encounter performance problems
# -> less memory, perform faster
# -> same data type
numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(0, 4)
numbers.pop()
numbers.remove(1)
# numbers[0] = 1.0 # cannot do this


# --- Sets ---
# unordered collections of unique items
# do not support indexing
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("yes")

# --- Dictionaries ---
# key value pairs
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])

print(point.get("a", 0))

del point["x"]
print(point)

for key, value in point.items():
    print(key, value)


## defaultdict
from collections import defaultdict

d = defaultdict(list)
d["key"].append("hello")


# --- Comprehensions ---
# [expression for item in items]
values = [x * 2 for x in range(5)]  # List
values = {x * 2 for x in range(5)}  # Sets
values = {x: x * 2 for x in range(5)}  # Dictionaries

# --- Generators ---
# when dealing with really large dataset
# generators have consistent size
values = (x * 2 for x in range(10000))
print("list:", getsizeof(values))
# for x in values:
#     print(x)
# print(len(values)) # not working
print("gen:", getsizeof(values))
values = [x * 2 for x in range(10000)]


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# --- Unpacking Operator
# unpack any iterable
numbers = [1, 2, 3]
print(numbers)
print(*numbers)

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)


# Time Complexity
# x in collection
# O(1): set, dict (implementation based on hash tables)
# O(n): list

# Ordered dict
from collections import OrderedDict

ordered_dict = OrderedDict({"a": 1, "b": 2})
ordered_dict.move_to_end("a")
print(ordered_dict.popitem(last=True))
