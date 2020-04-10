#一个类创建多个实例
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def increment_login_attempts(self, login_attempts):
        self.login_attemopts = login_attempts
        login_attempts += login_attempts
        return login_attempts

    def reset_login_attempts(self):
        self.login_attempts =  0

    def describe_user(self):
        print(self.last_name)
        print(self.first_name)

user1 = User('A', 'B')
user1.describe_user()
user1.increment_login_attempts(1)
