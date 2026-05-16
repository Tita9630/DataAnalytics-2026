class Restaurant:
    '''This class represents a restaurant.'''
    def __init__(self, rest_name, food_type): # initializing a class
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []
    def describe_rest(self): # method1
        print(f"{self.rest_name} serves {self.food_type}.")
    def rest_open(self): # method2
        print(f"{self.rest_name} is open")
    def add_num_served(self): # method 3
        customers = int(input("How many customers served today?"))
        self.number_served += customers
    def print_num_served(self): # method 4
        print(f"{self.rest_name} has served {self.number_served} customers.")
    def  customer_rating(self): # method 5
        while True: # keep asking untill user enters a valid rating
            rating = input("Rate your experience from 1-5: ")
            if rating.isdigit():
                rating = int(rating)
                if 1 <= rating <= 5:
                    self.customer_ratings.append(rating) # add ratings into the list
                    average = sum(self.customer_ratings) / len(self.customer_ratings) # Calculating the average
                    print(f"Your rating was {rating}.")
                    print(f"The average rating for this restaurant is {average}")
                    break # stop the look when a valid input is entered 
                else:
                    print("Please enter a number from 1-5.")
            else:
                print("Invalid input. Enter a whole number from 1-5.")
       
# creating restaurant objects
restaurant1 = Restaurant("Donkin Dunnts", "Donuts")
restaurant2 = Restaurant("Burger King", "Burgers")
restaurant3 = Restaurant("Subway", "Sandwiches")

# calling methods
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant1.customer_rating()
restaurant1.customer_rating()

restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant2.customer_rating()
restaurant2.customer_rating()


restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()

restaurant3.customer_rating()
restaurant3.customer_rating()