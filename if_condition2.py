#3/14/2021 if ststament continues chapter 5
num = 20
if num >= 1 and num <= 10:
    print(f"number is equal or greater than 1 and less than 10")
else:
    print(f"number is less than 1 or greater than 10.")

'''
#expression AND/OR expression AND/OR expression

OR: # anything with true is true 
True OR True = True
True OR False = True
False OR  True = True
False or False = False

AND: # in and case anything with False is false
True OR True = True
True OR False = False
False OR  True = False
False or False = False
'''
#expression OR expression = True or False = True
#where country= 'UK or country='USA >> True or False

# The if-elif-else (we going to use alot)

#age =int(input('enter the visitors:'))
age = 3
if 0 <= age <=4:
    print("uour admission cost is $0.") # just did unit testing by going each code
elif 4 < age < 18:
    print("your admisson cost is $5.")
elif 18 <= age <140:
    print("your admisson cost is $10.")
else:
    print("invalid age was entered, bye.")

#if I enter string like one I will have a error becouse I converted int
#age = int(input('enter the visitors:'))
#elif checks the condition

#age = int(input('enter the visitors age:'))
price = 0
if age < 4:
    price =0
elif age <18:
    price = 5
elif age < 140:
    price = 10
else:
    price =10
    print("invalid age was entered, bye.")
print(f"your admission cost is ${price}.")

#n , 0 < n < 2000000

print("---5-3----Aliena colors -------------")
#alien_color = input ('enter the elien color (green/yellow/red): ')
#if alien_color == 'green':
    #print(f"You just earned 5 points!!")
#elif alien_color == 'yellow':
    #print(f"you just earned 2 points, whee!")
#elif alien_color == 'red':
    #print(f" you just earned 10 points, you are killing it, man!!")
#else:
    #print("no points, sorry, take a rest, meditate.")

print("--------------------------")
friends = ()    # ifata structurelidt or tuples is emty the result will be true case
if friends:
    print("good for you, can I be your friend.")
else:
    print(f"Go out make some friends, only good friends.")

print('--------------Using Multiple list ------------')
# class home work
# // floor division -division ignoring the remainder
# % modulus -gives the remainder

print("Famouse interview question fuzzbzzz------------")
num = int(input("enter the number > 0:"))
#if (num % 3 == 0) and (num % 5 == 0):
    #print("Fuzzbuzz")
#elif num % 3 == 0:
    #print("fuzz")
#elif num % 5 == 0:
    #print("Buzz")



