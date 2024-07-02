# Create a list of person dictionaries with a name, age and list of hobbies for each person. Fill in data you want.
persons = [
    {
        "name": "Alvin",
        "age": 29,
        "hobbies": ["Sports", "Cooking"]
    },
    {
        "name": "Anna",
        "age": 19,
        "hobbies": ["Dancing", "Bowling"]
    },
    {
        "name": "Manu",
        "age": 33,
        "hobbies": ["Fishing", "Gaming"]
    }
]
# Use a list comprehension to convert this list of persons into a list of names
person_name = [person["name"] for person in persons]
print(person_name)
# Use a list comprehension to check whether all persons are older than 20
person_over_twenty = all([person["age"] > 20 for person in persons])
print(person_over_twenty)
# Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# copied_persons = persons[:] won't work
copied_persons = [person.copy() for person in persons]
copied_persons[0]["name"] = "Max"
print(copied_persons)
print(persons)
# Unpack the persons of the original list into different variables and output these variable
p1, p2, p3 = persons
print(p1)
print(p2)
print(p3)
