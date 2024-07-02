# import the random function and generate both a random number between 0 and 1 as well as a random number between 1
# and 10.
import random
import datetime

random_num = random.random()
print(random_num)

random_num2 = random.randint(1, 10)
print(random_num2)
# use the datetime library together with the random number to generate a random, unique value.
now = datetime.datetime.now()
ru = str(now) + str(random_num2)
print(ru)