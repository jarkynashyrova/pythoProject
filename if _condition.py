#if statements:
#if expression:
#    code here when expression is true
#else:
#    code here when expression is false

#num1_str = input("enter the num1:") # converting to intiger in two setps
#num1 = int(input("enter the num1:")) # same as above but in one step
num1 = 2
num2 = 3
if num1 < num2: # comparing two values using ==
    print("expression is true")
    print("you can do somthing here")
else:
    print ("expression is false") # this line didnt get executed becouse it was true case

print("---------second-----------")
msg = input("enter True/False")
if msg:
    print("expression in True")
    print("you can do somthing here")
else:
    print("expression in false")

print("---------third-----------")
#msg = 0 is cosesidered fale
#msg = 5 is true
if msg:
    print("expression in true")
    print("you can do somthing here")
else:
    print("expression in false")

print("---------fourth-----------")
num = 5
if num in range(3, 6, 2):
    print("expression in true, and num is within range")
    print("you can do somthing here")
else:
    print("expression in false")

print("---------fourth-----------")
num = 0
if num not in range(5):
    print("expression in true, and num is within range")
    print("you can do somthing here")
else:
    print("expression in false")

print("---------fifth-----------")
num = 0
if num !=0: # != means not = 0
    print("expression in true, and num is within range")
    print("you can do somthing here")
else:
    print("expression in false")

print("---------sixth-----------")
msg = input ("enter the number:")
if msg.strip() != '':
    print(" this message was entered: \n'{msg}'")
    print("you can do somthing here")
else:
    print("whitespace was entered")

print("---------seventh-----------")
msg = input ('enter the your name')
if msg.strip().lower == 'john doe':
    print(" this message was entered: \n'{msg}'")
    print("you can do somthing here")
else:
    print("whitespace was entered")

print("---------if statment with lists----------")
cars = ['bugatti','tesla', 'ferrari','lexus']
if 'tesla' in cars:
    print("yes, we have tesla in stock.")
else:
    print("sorry we dont have this car.")

print("--------if statment with strings-----------")
if 'sat' in "today is saturday":
    print("yes, it is satyrday.")
else:
    print("no, today is sunday")

print("-------if statment with lists and looping------------")
for car in cars:
    if car == 'tesla':
        print(f"This is {car.upper()}")
    else:
        print(f"current car is {car.title()}")

print("-------if statment with lists and looping with break to stop-----------")
for car in cars:
    if car == 'tesla':
        print(f"This is {car.upper()}")
        break
    else:
        print(f"current car is {car.title()}")

print("exersie-----------------")
nums = [45, 5, 6, 3, 10]
for num in nums:
    if num == 5:
        print(num,'completed')
        break # if you dont put break it will continue to print further saying 6 is not 5 and 3 is not 5 so on.
    else:
        print(num,'is not 5')

print("exersie how to count-----------------")
nums = [45, 5, 6, 3, 10, 5, 7, 8, 5, 666, 5]
count = 0
for num in nums:
    if num == 5:
        print(num,'completed')
        count = count = 5 +1
        break
    else:
        print(num,'is not 5')