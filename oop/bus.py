from vehicle import Vehicle


class Bus(Vehicle):
    # Constructor creates instance attributes
    def __init__(self, starting_top_speed=100):
        # calling the constructor of the Parent/Base class
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(150)
bus1.add_group(["Max", "Manuel", "Anna"])
bus1.add_warning("Test")
print(bus1.passengers)
bus1.drive()
