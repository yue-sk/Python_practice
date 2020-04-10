#继承类
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
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

#继承至Resraurant类
class IceCreamStand(Restaurant):
    #方法init接受创建父类实例所需的信息
    def __init__(self, restaurant_name, cuisine_type):
        #super是一个特殊函数，帮助python将父类和子类联系起来
        super().__init__(restaurant_name, cuisine_type)
        #存储一个由各种口味冰淇淋组成的列表
        self.flavors = []

    def show_flavors(self):
         print("\nWe have the following flavors")
         for flavors in self.flavors:
             print("-"+ flavors.title())

big_one = IceCreamStand('The Big One','ice_cream')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()

