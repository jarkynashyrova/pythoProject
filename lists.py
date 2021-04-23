# lists (Array) a list a collection of items in a particular order. you can make
# list that includes the letters, digits from 0-9 or names
# the pop() method removes the element
#append() add items to the list
#operations: create, access, add element, remove element, copy
#num = lists()# create an empty list
#evens = []  # create an empty list
num = 11
odds = [1, 3, 5, 7, 9,457] # 5 elements, size of 'odds list is 5 [element]
# index: 0, 2, 3, 4 ....
# n ind: -6 -5 -4 -3 -2 -1 # from back , there is no 0
# what is the element on index 2? it is 5, becouse indexing starts with 0
friends = ['jackson', 'said', 'linur', 'tyson'] # it is better to have same data type
print(friends)

# Access
first_friends = friends [0]
print(f"friends:{friends[0]}")
print(f"friends:{friends[2]}")
print(f"friends:{friends[3]}")
print(f"friends:{friends[-1]}")
print(f"friends:{friends[-3]}")

# adding alemnts: Adding to the list
# list.append(new_element) - this new_element to end of the list
# list.insert(index, new_elemnts) this adds new_elemnts
# add tp a friend list
friends.append('obama') # append is better to use than insert to add value
print(f"new friends lists:{friends}")
friends.insert(0, 'messi')
friends.insert(0, 'Ronaldo')
print(f"new friends list after insert:{friends}")

#restetting the existing element, only existing index should be used
friends[2] = 'mark' # replaces Tyson with mark
print(f"new friends list after reset:{friends}")
#friends[7] = 'mark' # replaces Tyson with mark
#print(f"new friends list after reset:{friends}")
# to comment do >>ctrl + /

#remove the elements by value , by index
friends.remove('mark') # by value
print(f"new friends list after removing 'mark': {friends}")
#remove_one1 = friends.remove('mark')  - this is not valid statment, since remove() does not return anything
# print(remove_one1)
removed_friends =[]
remove_one = friends.pop(4)

friends.pop(4) # pop function returns(informs) what is it is removing
print(f"new friends list after popping index 4: {friends}")

del friends[-1]
print(f"new friends list after del index -1: {friends}")

friends = []
print(f"new friends list after redefining:{friends}")


names = ['Irma', 'Daria','Elizabeth','OLga']
print(names [0])
print(names [1])
print(names [2])
print(names [3])
# 3-2
names = ['Irma', 'Daria','Elizabeth','Olga']
removed_guests=[]
print('***************************see removed guest')
removed_guests.append(names.pop())
print(removed_guests[-1] + ",I am sorry I can't invite you for dinner.")
print(removed_guests)

removed_guests.append(names.pop(0))
print(removed_guests[-1] + ",I am sorry I can't invite you for dinner.")
print(removed_guests)
print(names)


message = "I am sorry that I can't invite you for my dinner party " + names [0] + "."
print(message)
print(names.pop(-1) + ", I am sorry that I can't invite you for my dinner party. ")

#3-3
cars = ['Jeep', 'Tesla', 'Range' 'bmw']
print(cars)
message = "I would like to own a " + cars [0].title() + "."
print(message)

#3-4
print("*******************guest list************************")
Family = ['Father', 'Grand Father', 'taine', 'Taita']
print(Family)
print(f"Hi {Family [0].title()}, I would like to invite you to Family dinner.")
print(f"Hi {Family [1].title()}, I would like to invite you to Family dinner.")
print(f"Hi {Family [2].title()}, I would like to invite you to Family dinner.")
print(f"Hi {Family [3].title()}, I would like to invite you to Family dinner.")

#3-5
print(f"Hi {Family [0].title()}, my Grand father cant make for family dinner tonight.")
Family [1] = 'Sultan Ata'
print(f"New dinner guest list after reset:{Family}")
print(f"Hi {Family [1].title()}, I would like to invite you to Family dinner.")

#3-6
Family.insert(0,'Tyigun')
print(f"New Family dinner list after insert:{Family}")
Family.insert(3,'chon apa')
print(f"New Family dinner list after insert:{Family}")
Family.append('taike')
print(f"New Family dinner list after append:{Family}")
print(f"Hi {Family [0].title()}, I would like to invite you to Family dinner.")

#3-7

Family.pop(4)
print(f"new Family list after popping index 4: {Family}")
print("first pop")
Family.pop(-2)
print(f"new Family list after popping index -2: {Family}")
Family.pop(2)
print(f"new Family list after popping index 2: {Family}")
print(f"Hi {Family [0].title()}, you are still invited  to Family dinner.")
print(f"Hi {Family [1].title()}, you are still invited to Family dinner.")
del Family [0]
print(f" Family list after del last two after index 0: {Family}")
del Family [-1]
print(f" Family list after del last two after index -1: {Family}")

print("****************** 03/07/2021 # orgonizing the list ****************")
# sorting the list permanently
names = ['Irma', 'Daria','Elizabeth','OLga']
print(names)
names.sort() # changing the list in desending order for original list
names.sort(reverse=True) # changing the list sorting in descending order
print(names)

#sorting the list temperarily and returning the copy of sorted list
cars = ['Audi', 'Tesla', 'Range', 'BMW']
sorted_cars_asc = sorted(cars)
sorted_cars_desc = sorted(cars,reverse = True)
print(f"cars: {cars}")
print(f"sorted_cars_asc: {sorted_cars_asc}")
print(f"sorted_cars_desc: {sorted_cars_desc}")

# reverese is used otherway around, oposite
cars.reverse() # reverses the list
print(f"cars: {cars}")

sorted_cars_asc2 = sorted(cars)
print(sorted_cars_asc2)
sorted_cars_asc2.reverse()
print(sorted_cars_asc2)

# abstruct thinking is tested on solving some coding problems
#list, sum()
list_size = len(cars)
print(f"list_size: {list_size}")

#3-8

locations=['London', 'Australia', 'Germany', 'Crotia']
print(locations)
print(sorted (locations))
print(locations)
#locations.reverse()
print(sorted(locations, reverse = True))
print(locations)

# none: null in sql
# object: evrything is an abject in the python (charcater, file, string, variable, list, fucntions,etc)
# iterable: something that