# write a normal function that accepts another function as an argument and output the result of the other function in
def normal_func(func):
    print(func(10))


# your normal function call your normal function passing lambda function
normal_func(lambda data: data * 2)


# tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed
def normal_func2(fn, *args):
    for arg in args:
        print(fn(arg))


normal_func2(lambda data: data * 10, 15, 22, 30)


# format the output of your normal function such that numbers look nice and are centered in a 20 character column
def normal_func3(fn, *args):
    for arg in args:
        print("Result: {:^20.2f}".format(fn(arg)))


normal_func3(lambda data: data * 10, 15, 22, 30)
