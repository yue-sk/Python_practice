#返回字符串
def city_country(name,country):
    cityname = name.title() + ','+ country.title()
    return cityname


cityname= city_country("Santiago","Chile")
print(cityname)