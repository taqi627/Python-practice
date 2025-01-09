city = 'Sukkur','Hala','Karachi'

print(type(city))

(a,b,c) = city

print(a)
print(b)
print(c)

cities = list(city)

cities.append('Hyderabad')

city = tuple(cities)

print(type(city))
print(city)