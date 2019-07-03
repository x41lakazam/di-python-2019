import time


def timer_teacher(function_address):

    # Defining the new function
    def timed_function():
        before = time.time()
        res = function_address()
        after = time.time()
        print("Function {} took {} seconds".format(function_address.__name__, after-before))
        return res

    return timed_function


@timer_teacher
def long_function():

    i = 0
    for index in range(50000000):
        i += index
    return i 

@timer_teacher
def really_long_function():
    i = 0
    for index in range(10000):
        for index_2 in range(10000):
            i += index + index_2
    print(i)


really_long_function()
long_function()

print("Finish")
