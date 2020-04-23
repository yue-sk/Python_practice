#setUp()方法
#输入于输出是否一致
#输入与预想的输出是否一致；
import  unittest

class Employee():
    """Initialize the employee"""
    def __init__(self,firstname,secondname,salary):
        self.firstname = firstname
        self.secondname = secondname
        self.salary = salary

    def give_salary(self,amount = 5000):
        """Give the employee a raise"""
        self.salary += amount

class TestEmploee(unittest.TestCase):
    def setUp(self):
        self.Eric = Employee('Eric','matthes','6500')

    # def test_give_default_raise(self):
    #     self.eric.give_raise()
    #     self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 5000)

unittest.main()







