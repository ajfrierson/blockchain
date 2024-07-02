# the "with" keyword allows you to work with a file and have python close it automatically
with open("demo.txt", mode="r") as file:
    # file_content = file.write("add this content\n")
    # file_content = file.readlines()
    # file.close()
    #
    # for line in file_content:
    #     print(line[:-1])

    print(file.readline())

print("done")


