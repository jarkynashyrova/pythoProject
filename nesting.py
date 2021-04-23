#03/21/2021
#1. A list of Lists
#2. A list of Dictionaries
#3. A List ina Dictionary
#4. A dictionary in Dictionary

countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies =['level up', 'abc company',' ola company']

customers = [companies, cities, countries]
print(customers [0])
print(customers [0][1])
print(f"print barcelona:{customers [1][2]}")

multi_dim_nums = [
   [3, 9, 0],
   [2, 7, 1],
   [0, 1, 0]
]
print(f" print the middle value {multi_dim_nums[1][1]}")

print(" \nnested Loops: looping through the middle value(array).")
for column in customers:
   print(column)
   #[['level up', 'abc company','ola company']
   for value in column:
      print(value.upper())

for city in customers [1]:
   print(city,end = '\t')

print("\n******************* list of dictionaries*************")
user_0 = {'name':'john', 'age':25, 'city':'brooklyn'}
user_1 = {'name':'jane', 'age':20, 'city':'paris'}
user_2 = {'name':'mark', 'age':35, 'city':'tokyo'}

users = [user_1, user_0, user_2]
print(users[0])
print(users[2]['name']) # prints Mark
print(users[2]['age'])# marks age
print(users[2]['city'])# marks city

print("---------looping---------------")
for user in users: # multiplication table we can use in this form
   print(user['name'], end=' || ')
   print(user['age'], end=' || ')
   print(user['city'])

print("************\n list in a Dictionary**********")
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies =['level up', 'abc company',' ola company']

customers = {
   'countries': ['usa', 'russia', 'spain'],
   'cities': ['new york', 'moscow', 'barcelona'],
   'companies': ['level up', 'abc company',' ola company']
}

print(customers['cities'])
print(customers['cities'][1])# second element from cities


print("***********\n Dictionary in a Dictionary*********")

user_0 = {'name':'john', 'age':25, 'city':'brooklyn'}
user_1 = {'name':'jane', 'age':20, 'city':'paris'}
user_2 = {'name':'mark', 'age':35, 'city':'tokyo'}

users = {
   'user_0': {'name':'john', 'age':25, 'city':'brooklyn'},
   'user_1': {'name':'jane', 'age':20, 'city':'paris'},
   'user_2': {'name':'mark', 'age':35, 'city':'tokyo'}
}
print(users)
print(users['user_0'])
print(users['user_0']['name'])

#for user in user.keys():
#   print(user)
#   print(users[user])

for username, details in users.items():
   print(username)
   #print(details['name'])
   for key, value in details.items():
      print(f"details key is: {key}")
      print(f"details value is :{value}")




