class Vehicle:
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        # __ makes an attribute private providing some encapsulation
        self.__warnings = []

    def get_warnings(self):
        print(self.__warnings)

    def __repr__(self):
        print("Printing...")
        return "Top Speed: {}, Warnings: {}".format(self.top_speed, len(self.__warnings))

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def drive(self):
        print("I am driving but certainly not faster than {}".format(self.top_speed))