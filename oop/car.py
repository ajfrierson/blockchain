""" This is how you implement inheritance in Python"""
from vehicle import Vehicle


class Car(Vehicle):
    # Class Attributes
    # top_speed = 100
    # warnings = []

    # Constructor creates instance attributes

    def brag(self):
        print("Look how cool my car is!")


car1 = Car()
car1.drive()

car1.add_warning("New warning")
# car1.__warnings.append([])
# the __dict__ dunder (short for double under) is used to show object attributes as a dictionary.
# Won't include methods.
# print(car1.__dict__)
print(car1)
car2 = Car(200)
car2.drive()
print(car2.get_warnings())

car3 = Car(250)
car3.drive()
print(car3.get_warnings())
