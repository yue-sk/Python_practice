#一个类创建多个实例
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.last_name)
        print(self.first_name)

    def greet_user(self):
        print(self.first_name + "hello")

user1 = User('A','B')
user1.describe_user()
user1.greet_user()
