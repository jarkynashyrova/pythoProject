## 02/20/2021 Looping through dictionay

my_car = {"brand":"ford", "model":'Mustand',"year": 1964}
for key in my_car:
    print("-------------------------------")
    print(f"key in this iteration is:{key}")
    print(f"value in this key is : {my_car[key]}")

print("-2----")
for key in my_car.keys():
    print("-2-------------------------------")
    print(f"key in this iteration is:{key}")
    print(f"value in this key is : {my_car[key]}")

if 'model' in my_car:
    print(f"yes my_car desc contains model information")

print("-3 using dic.values()---------------------------------")
for value in my_car. values():
    print("--------------------------------")
    print(f"value in this iteration is: {value}")
    #print(f"of this key is :{my_car[value]}")

print("-4 using dic.items()--# most people use-------------------------------")
for key, value in my_car.items():
    print("--------------------------------")
    print(f"val1 in this iteration is: {key}")
    print(f"val2 in this key is: {value}")

if 1964 in my_car.values():
    print(f"yes my_car desc contains 1964 information")

print("*******- with list sort(), sorted(list)---------")
friends = ['john', 'jane']
print(friends)
sorted_friends = sorted(friends) #sorted will not effect your original list
friends.sort()#can not assighn to variable since it sorts original list
print(sorted_friends)
print(friends)

farvorite_language ={'jen':'python','sarah':'c', 'edward': 'ruby', 'phil':'python'}
print("******** sorted list*********************************")
for name in sorted(farvorite_language.keys()):
    print(f"{name}'s favorite language is {farvorite_language[name]}")


print("----6-5---------")
rivers = {'nile': 'egypt', 'tigris': 'iraq', 'amazon': 'south america' }
for river, country in rivers.items():
    print(f" The {river.title()} runs through {country.title()}.")