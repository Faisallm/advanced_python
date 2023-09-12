

# when we can't use the range function
# when we are trying to do something...
# that exceeds the capabilities of the
# range function, we have to build our
# own generator.

import sys


def mygenerator(n):
    for x in range(n):
        yield x ** 3


values = mygenerator(10000000)
# we won't get the entire value at the same time,
# but instead we use a generator that returns
# the next value whenever we need it.
# on-demand

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# we can also do it with iteration
# for x in values:
#     print(x)

print(sys.getsizeof(values))


# with generators, we can create infinite sequences.

def infinite_sequence():
    # a limitless sequence
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()


print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))