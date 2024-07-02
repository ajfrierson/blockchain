class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return "Name: {}, Kind: {}".format(self.name, self.kind)

    def describe(self):
        print("I am a {}, and I am considered to be a {}.".format(self.name, self.kind))
#
#
# banana = Food("Banana", "fruit")
# pork = Food("Pork", "meat")
# pork.describe()
# banana.describe()

"""Converted to a class method that we can call directly on the class itself"""

#
# class Food:
#     name = 'X'
#     kind = "Y"
#
#     # def __init__(self, name, kind):
#     #     self.name = name
#     #     self.kind = kind
#     @classmethod
#     def describe(cls):
#         print("I am a {}, and I am considered to be a {}.".format(cls.name, cls.kind))
#
#
# Food.name = "Banana"
# Food.kind = "fruit"
# Food.describe()

"""Converted to a static method that we can call directly on the class itself"""


# class Food:
#     name = 'X'
#     kind = "Y"
#
#     # def __init__(self, name, kind):
#     #     self.name = name
#     #     self.kind = kind
#     @staticmethod
#     def describe(name, kind):
#         print("I am a {}, and I am considered to be a {}.".format(name, kind))
#
#
# Food.describe("Apple", "fruit")
