simple_list = [1, 2, 3, 4]
simple_list.extend([5, 6, 7])
del simple_list[0]
print(simple_list)

d = {"name": "Max"}
print(d.items())
del d["name"]
print(d)
for k, v in d.items():
    print(k, v)

t = (1, 2, 3)
print(t.index(1))

s = {"max", "anna", "max"}
print(s)

"""Map() function that does something for every element of a list """
simple_list = [1, 2, 3, 4, 5]
# the lambda function allows you to write single line functions
print(list(map(lambda el: el * 2, simple_list)))

""" functools.reduce() is a function that reduces an iterable to a single value"""


# functools.reduce(function, iterable[, initializer])

# the asterisk task the comma separated values and turns them into a tuple
# which we can then use to pass as many arguments as we'd like
def unlimited_arguments(*args):
    for argument in args:
        print(argument)


unlimited_arguments(1, 2, 3, 4, 5)


# you can do the same thing for dictionaries using **keyword_args
def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for argument in keyword_args.items():
        print(argument)


unlimited_arguments(1, 2, 3, 4, name="Alvin", age=48)
