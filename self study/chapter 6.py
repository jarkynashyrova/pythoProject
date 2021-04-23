#Dictionary storied information  in key- value pair.

alien_0 = {'color': 'green', 'points': 5}
# color is Key
# green is value

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print("-----------------modify values in dictionary----------------")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

print("\n-------6-1------------------")
user_0 = {'last':'ashyrova','first':'jackie','city':'NYC'}
print(user_0)

for key,value in user_0.items(): # using
    print("\nKey: " + key)
    print("Value: " + value)

print("------------6-2------------")
number = {"irma":3, "Elizabeth":2,"olga":1,"maky":4}
print(f"My friend irma's favorite number is {number['irma']}")
print(f"My friend Elizabeth's favorite number is {number['Elizabeth']}")
print(f"My friend Olga's favorite number is {number['olga']}")
print(f"My friend maky's favorite number is {number['maky']}")

print("\n-----looping through all key-value pairs--------")
for name, number,in number.items():
    print(name.title() +' loves ' + str(number))



print("------------6-3---------------")
glossary = {
    ".append()":"this adds new element to end of the list",
    ".remove()":"removes but does not return anything",
    "del":"delets from the list",
    ".sort()":"changing the list in ascending order"
    }
print(f".append(): \n\t"
      f"{glossary['.append()']}")
print(f".remove(): \n\t{glossary['.remove()']}")
print(f"del: \n\t{glossary['del']}")
print(f".sort():\n\t {glossary['.sort()']}")

print("------------6-4 loop through a dic.---------------")
print("\n--looping through all- key value everything stored in glossary dictionary at once-----")
for key, value in glossary.items():
    print("\nKey: " + key)
    print("Value: " + value)
print("\n--- adding key values after looping--------")
glossary['reverse'] = 'reverses the list'
print(glossary)

print("------------6-5 .---------------")
rivers = {'nile':'egypt','tigris':'iraq','amazon':'south america',}
for river in rivers.keys():
    if river in rivers:
        print(" The " + river.title() +
             " runs through " +
              rivers[river].title())
print("----6-5---------")
rivers = {'nile': 'egypt', 'tigris': 'iraq', 'amazon': 'south america', }
for river, country in rivers.items():
    print(f" The {river.title()} runs through {country.title()}.")

rivers['Michigan']= 'chicago'
print(rivers)

print("---6-7---")
user_0 = {'last':'ashyrova', 'first':'jackie', 'city':'NYC'}
user_1 = {'last':'Auhing', 'first':'elizabeth', 'city':'german'}
user_2 = {'last':'Gorbo', 'first':'irma', 'city':'Bosnia'}

users = [user_1, user_0, user_2]
print(users)
for user in users:
   print(user['last'], end=' || ')
   print(user['first'], end=' || ')
   print(user['city'])
print(" ------ex 6-8----------------------------")
cat = {'name': 'bobkie', 'age': '3', 'color': 'black'}
dog = {'name': 'mamba', 'age': '5', 'color': 'brown'}
horse = {'name': 'jokie', 'age': '2', 'color': 'white'}
pets = [cat,dog,horse]
for pet in pets:
   print(pet['name'], end=' || ')
   print(pet['age'], end=' || ')
   print(pet['color'])

print("------------6-10 modifing 6-2------------")
number = {"irma":(3, 4), "Elizabeth": (2,3),"olga":(1, 5),"maky":(4, 6)}
print(f"My friend irma's favorite number are {number['irma']}")
print(f"My friend Elizabeth's favorite number are {number['Elizabeth']}")
print(f"My friend Olga's favorite number are {number['olga']}")
print(f"My friend maky's favorite number are {number['maky']}")

print("\n-----looping through all key-value pairs--------")
for name, number,in number.items():
    print(name.title() +' loves ' + str(number))

print("----------6-11----------")
cities={
    'NYC' : {'country':' NY', 'population':10, 'fact':'bigest city in the America'},
    'Washington_DC' : {'country':'Capital', 'population': 2, 'fact':'home for usa president'},
    'Miami' :{'country':'Florida', 'population':3, 'fact':' nice weather all year around'}
}
print(cities)
print(cities['NYC']),
print(cities['Washington_DC']),
print(cities['Miami'])

print("---------6-12 adding a key and value ---------")






