cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw': # if the current value of the cars is BMW
        print(car)
        break
    else:
        print('car')

print("------------conditional test is True/False---------------")
#The simplest conditional test checks whether the value of a variable is equal
# to the value of interest in python console
# >>> car =='bmw'
answer = 2022
if answer != 2021:
    print("that is not the correct asnwer. Please try one more time")

print("-------------Checking Whether a Value Is Not in a List-----------")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post response if you wish.")
#5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#5-2
age = 35
print("is age == 35? if no please welcome to the club!")
age == 35

print("---------------If statments-------------")
print("if -elif function-------------------------------------")
# Often, you’ll need to test more than two possible situations,
# and to evaluate these you can use Python’s if-elif-else syntax
# you can ue elif blocks as much as possible
# Python does not require an else block at the end of an if-elif chain.
#The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass.
# As soon as Python finds one test that passes, it skips the rest of the tests.
age = 100
if age <= 20:
    print("Congrutulations!")
elif age <= 40:
    print("wellcome!")
else:
    print("sorry, you are not allowed to the club")
print("pizza example -------------")
requested_toppings = ['mushrooms', 'extra cheese']



