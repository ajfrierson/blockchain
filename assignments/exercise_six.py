# write a short python script which queries teh user for input (infinite loop)
# user should be able to output data from the file
# running = True
# while running:
#     print("Please choose: ")
#     print("1: Add input: ")
#     print("2: Output data")
#     print("q: quit")
#     user_input = input("Your choice: ")
#     if user_input == "1":
#         data_to_store = input("Your text: ")
#         with open("assignment.txt", mode="a") as file:
#             file.write(data_to_store)
#             file.write("\n")
#             """ Outputting data from the file"""
#     elif user_input == "2":
#         with open("assignment.txt", mode="r") as file:
#             file_content = file.readlines()
#             for line in file_content:
#                 print(line)
#     elif user_input == "q":
#         running = False
import json

running = True
user_input_list = []
while running:
    print("Please choose: ")
    print("1: Add input: ")
    print("2: Output data")
    print("q: quit")
    user_input = input("Your choice: ")
    if user_input == "1":
        data_to_store = input("Your text: ")
        user_input_list.append(data_to_store)
        with open("assignment.txt", mode="w") as file:
            file.write(json.dumps(user_input_list))
    elif user_input == "2":
        with open("assignment.txt", mode="r") as file:
            file_content = json.loads(file.read())
            for line in file_content:
                print(line)
    elif user_input == "q":
        running = False

