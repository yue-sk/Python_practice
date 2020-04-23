import unittest

def city_country(city, country,population):
    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return   output_string


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

unittest.main()