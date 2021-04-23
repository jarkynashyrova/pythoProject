# looping though an entire list
# The concept of looping is important because it’s one of the most -
# - common ways a computer automates repetitive tasks

print ("--------looping---------")
magicians = ['alice', 'david','carorlina']
for magician in magicians: # we define a for loop
    print(magician)

print ("--------list----------")
magicians = ['alice', 'david','carorlina']
print(magicians) # this is just a list

print("doing more work within a for loop------")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

dears = [ 'Mather', 'Zalkar', 'Ainur', 'Makzura', 'Azamat', 'Meerim']
for dear in dears:
    print(dear + ", I am getting married finaly")
    print("I cant wait to see you at my wedding, " + dear + ".")
    print("please bring your husband, children and wife, " + dear + ".\n" )

print(" ------looping-------- ")
magicians = ['alice', 'david', 'caralina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I cant wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!") # not indented line this is printed just once

print("----------Homework----------")
#4-1

pizzas = ['Margarita','Plain','Artichoke']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("I really love pizza!.")

print("----4-2-------")

animals = [ 'dog', 'cat', 'horse']
for animal in animals:
    print(animal.title() + ", would make a great pet.")

print("any of these animals would make a great pet.")

print("-----------making numerical List-----------")

print("---------using range() functions-----------")
for value in range(1,6): # to print the numbers from 1 to 5 you would use (1,6)
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

print("---in python two asterisks(**) represent exponents--")
squares =[]
for value in range (1,11):
    square = value **2
    squares.append(square)

print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

print("-------simple statistics with a list of numbers---------")

squares = [value **2 for value in range (1,11)]
print (squares)

print("--------slicing a list----------")

players = ['charles','martina', 'michael', 'florence', 'eli']
print(players[0:3])

## looping through a slice

players = ['charles','martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("--------copying a list--------")

my_foods = ['pizza', 'falafal', 'cake']
friend_foods = my_foods[:]

print("my favorit food are:")
print(my_foods)

print("\nmy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food are:")
print(my_foods)

print("\nmy friend's favorite foods are:")
print(friend_foods)

print("----4-10-------")

foods = ['pizza', 'falafal', 'cake','apple','rice']
print(foods[:3])
print(foods[-3:])
print(foods[2:6])

## 4-11

friend_pizzas = ['Margarita','Plain','Artichoke']
friend_pizzas.append('peperoni')
pizzas.append('NY Pizza')

print(friend_pizzas)
print(pizzas)

for pizza in pizzas:
    print("my favorite pizzas are:")
    print(pizzas)
print("----------4-13--------")
# 4-13
buffets = ('fries', 'soup', 'salad', 'fish','sushi')
for buffet in buffets:
    print(buffet)

## MODIFY ONE OF THE FOOD

buffets = ('salmon')
print("\nmodified buffets:")
for food in foods:
    print(food)

for num in range(10,21):### we dont have to have list
    print(num**2)









