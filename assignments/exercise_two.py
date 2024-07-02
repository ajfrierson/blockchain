# Create a list of names and use a for loop to output the length of each (len())
names = ["Max", "Anna", "Manuel", "Chris", "Stephen"]

for name in names:
    if len(name) > 5 and ("n" or "N" in name):
        print(name)

# Add an if check inside the loop to only output names longer than five characters
while len(names) >= 1:
    print(names.pop())
    print(names)

# Add another if check to see whether a name includes a "n" or "N" character combine with task number 2.


# Use a while loop to empty the list of names via pop().
