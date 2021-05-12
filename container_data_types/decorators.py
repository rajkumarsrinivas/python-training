# # to understand what a decorator is first lets start with a closure.
# def times_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier

# three_times = times_of(3)

# # three_times(x):
# #     return x * 3

# five_times = times_of(5)

# print(three_times(9))

# print(five_times(3))

# print(five_times(three_times(2)))


# it is also possible to achieve the same using class and object.
# its upto us to decide whether to take the oop way or functional way.


#Decorators
#adding extra functionality of an existing function.

def display(func):
    def inner():
        print("starting decoration")
        func()
        print("ending decoration")

    return inner

@display
def printer():
    print("hello world")

printer()
# func  = display(printer)
# func()

#chaining of decorators.. using *args, **kwargs
#example not described.
