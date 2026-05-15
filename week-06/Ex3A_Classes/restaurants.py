class Restaurant:
    '''This class represents a restaurant.'''
    def __init__(self, rest_name, food_type): # initializing a class
        self.rest_name = rest_name
        self.food_type = food_type
    def describe_rest(self): # method1
        print(f"{self.rest_name} serves {self.food_type}.")
    def rest_open(self): # method2
        print(f"{self.rest_name} is open")
# creating restaurant objects
restaurant1 = Restaurant("Donkin Dunnts", "Donuts")
restaurant2 = Restaurant("Burger King", "Burgers")
restaurant3 = Restaurant("Subway", "Sandwiches")

# calling methods
restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()