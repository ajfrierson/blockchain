# create two variables - one with your name and one with your age
# create a function that returns your input as a concat string
# create a function that returns any data as a concat string
# create a function that returns how many decades you've been alive

age = "48"
name = "Alvin"


def name_and_age():
    print("Hi, my name is " + name + " and I am " + age + " years old.")


name_and_age()


def return_any_data_as_string(month, year):
    print("Today is " + month + ", " + year)


return_any_data_as_string("June", "2024")


def how_many_decades(_age):
    decades = _age //10
    return decades


print(how_many_decades(48))
