# 03/18/2021
# key value pair structure = dictionaries and key is unique but value is not
# Create, access, modify, ( add/remove/update element)
# looping this data structure
# some mostly used built in functions
# no indexing in dictionraies
my_friend = {} # creating an empty list
my_house = dict()
my_car = {"brand":"ford","model":"Mustang","year":1964, 1: 'val'}

print(my_car['brand'])
print(f" the value of the key 'brand' is:{my_car['brand']}.")
print(my_car[1]) # this is not an index, my car has  key=1

print("------------adding a key and value---------------")
my_car['price']= 12500.00
print(my_car)

print("---------updating the value in dictionaries-----------")
my_car['price']= 13000.00
print(my_car)

print("----------removing the value 1 from dictionaries---------")
del my_car[1]
print(my_car)

print("---------class excersize---------------------------")
person = {"name": "jose","last_name": "Davis","age":40,"city": "NYC"}
print(f"my friends first name is: {person ['name']}")
print(f"my friends last name is : {person ['last_name']}")
print(f"my friends age is: {person ['age']}")
print(f"my friends  lives city in: {person ['city']}")

".sort(reverse= true)":"sorting in descending order",