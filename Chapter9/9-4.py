#使用类和实例
#创建一个饭馆的类
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type,):
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.restaruant_name + "served wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def opn_restaurant(self):
        msg = self.restaruant_name + " is open"
        print("\n" + msg)

    #设置就餐人数
    def set_number_served(self,number):
        self.number_served = number

    #将就餐人数递增
    def increment_number_served(self,addtional_served):
        self.number_served += addtional_served
        return self.number_served


restaurant = Restaurant('A','B')
restaurant.describe_restaurant()
restaurant.opn_restaurant()
restaurant.set_number_served(30)
print(str(restaurant.number_served))
print(restaurant.increment_number_served(20))
