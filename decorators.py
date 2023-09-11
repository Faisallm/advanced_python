# # The basic idea behind generators is that they add a basic functionality
# # to a function without coding that functionality into the function
# # directly.

# # this is used to decorate other functions
# def mydecorator(function):

#     # this is the wrapper function
#     def wrapper(*args, **kwargs):
#         print("I have decorated your function!")
#         return_value =  function(*args, **kwargs)   # the function we are trying to decorate
#         return return_value

#     # we are actually returning another function that
#     # executes the initial function but with decoration.
#     return wrapper


# # this decorator will take this function as an argument.
# @mydecorator
# def hello(person):
#     return f'Hello {person}!'

# # calling the returned wrapper function
# # this is not actually the way we do it in python
# # mydecorator(hello_world)()


# print(hello('Faisal'))



# First Practical Example
def logged(function):

    def wrapper(*args, **kwargs):
        # get the return value of the function
        value = function(*args, **kwargs)
        # open a logfile in append mode
        with open('logfile.txt', 'a+') as f:
            # so this is how to get a functions name.
            fname = function.__name__
            # write to the logfile
            print(f'{fname} returned value {value}')
            f.write(f'{fname} returned value {value}\n')
        return value
    
    return wrapper

@logged
def add(x, y):
    return x + y

# print(add(10, 20))

