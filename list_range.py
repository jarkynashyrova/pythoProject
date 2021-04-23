# 03/11/2021 - Litst ( continue)

cars = ['Bugatti','ferrari', 'tesla', 'lexus']
#making nurical list with range () fucntions
# range (start, stop, step) -Return an obkect that produces a sequences of intiger from start
#-(
for num in range (4):
    print(num)
#shift + F6 - shortcut for refactor
# ctrl + Y -delere the line
nums = range (4) # this does not mean nums =[0,1,2,3]
nums2 = list(range(4)) # this creates list data structure from sequence of numbers
print(nums)
print (nums2)

print(nums2)
for num in nums2:
    print(num)

print ("range with start and stop----")
for num in range (1,4):
    print(num)

print("range with start and step----") # skip in between numbers 1+3=4+3=7 +3 = 10 but it will show 9 as last number
for num in range(1, 10, 2):
    print(num)

evens = []
print ("print all even numbers from 1 - 16 ( 16 should be included)")
for num in range (2, 17, 2):
    print(num)
    evens.append(num)
    print(evens)

print(f"This is the final list: {evens}")

print("_______________ Exerciese1 _____________________")
squares = list()
print ("print  the numbers square of numbers from 10 to 20")
for num in range(10, 21):
    squares.append(num**2)
print(squares)

# min, max, ave
print(f"final list :{squares}")
print(f"min list :{min(squares)}")
print(f"max list :{max(squares)}")
print(f"sum list :{sum(squares)}")

cars = ['Bugatti','ferrari', 'tesla', 'lexus''bmw']
cars_len = len(cars)
for car in cars:
    print(cars)
    print(f"index of the {car} is {cars.index(car)}")

print("loooping the list using index ---------------------")
for ind in range(len(cars)):
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")

# list comprehansion

squares = list()
for num in range (10,21):
    squares(num**2)

print(squares)

squares = [num**2 for num in range (10,21)] # for real only now, use later
print(squares)

