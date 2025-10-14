# --- Classes ---
class Point:
    # class attribute (shared across all instances of a class)
    default_color = "red"

    # Constructor, magic method
    def __init__(self, x, y):
        # instance attributes
        self.x = x
        self.y = y

    # other magic methods
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # class method -> factory method
    @classmethod
    def zero(cls):
        cls.default_color = 'x'
        return cls(0, 0)

    # static method -> utility method, cannot access/modify class state
    @staticmethod
    def say_hello(value: str):
        print(f'Hello {value}')

    # instance method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        self.say_hello("Point")


Point.default_color = "yellow"

point = Point(1, 2)
print(point)
point.draw()
print(point.x)
print(type(point))
print(isinstance(point, Point))
print(point.default_color)
print(Point.default_color)

# we can define an attribute after we create the object
# objects in Python are dynamic
# don't have to define all the attributes into the constructor
point.z = 10

other = Point(3, 4)
other.draw()
print(other.default_color)

# class method
point = Point.zero()
point.draw()
print(str(point))

# magic methods
# comparing objects
point = Point(1, 2)
other = Point(2, 3)
print(point == other)
print(point > other)
print(point < other)

# arithmetic operations
combined = point + other
print(combined)


# __new__ method will be called when an object is created then
# __init__ method will be called to initialize the object
class A(object):
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("Init is called")


a = A()