
import unittest

def get_City(City,Country):
    print("City:" + City)
    print("Country:" + Country)

get_City('Santigo','Chile')

class NameTestCase(unittest.TestCase):
    """测试cities.py"""
    def test_city_Cse(self):
        santigo_chile = get_City('Santigo','Chile')
        self.assertEqual(santigo_chile,'Santigo','Chile' )



unittest.main()