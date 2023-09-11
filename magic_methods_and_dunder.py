# # Dunder stands for double underscores -> __dunder__, __str__, __iter__
# # the __init__ method is an example of a dunder method.

# class Person:

#     # constructor
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # destructor
#     def __del__(self):
#         print("Object is being deleted!")

#     # this dunder method will be called when we use
#     # the print method on an object of this class.
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"


# # this is how we call the __init__ method.
# # __init__() method is not called like a regular method.
# p = Person("Faisal", 25)
# print(p)
# print(p)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # returning a new vector when we add two
        # vectors together.
        return Vector(self.x + other.x, self.y + other.y)

    # __repr__() is the official string representation
    # aimed at programmers as they develope and maintain
    # a program

    # __str__() is teh informal string representation,
    # a friendlier format for the program's user

    # def __str__(self):
    #     return f"x: {self.x}, y: {self.y}"

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

    def __len__(self):
        """it automatically triggers when you apply the
        length function to an object."""
        return 10

    def __call__(self):
        """in Python, we can call objects like functions."""
        print(f"Hello! I was called!, x: {self.x}")


v1 = Vector(10, 20)
v2 = Vector(20, 30)
v3 = Vector(1, 1)

v4 = v1 + v2
print(v4.x)
print(v4.y)
print(v4)
print(len(v4))
# In python, we can call objects like functions
# using the __call__ dunder method.
v4()
