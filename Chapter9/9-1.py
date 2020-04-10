#类
class Restaurant( ):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.describe_restaurant)
        print(self.cuisine_type)

    def opn_restaurant(self):
        print("is open")

restaurant = Restaurant('A','B')
restaurant.describe_restaurant()
restaurant.opn_restaurant()