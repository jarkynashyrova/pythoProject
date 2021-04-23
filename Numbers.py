# You can add (+), subtract (-), multiply (*), and divide (/) integers in Python

message = ("happy " + str(35) + "rd Birthday!")
print (message) # python knows that you want to convert the numerical value 23 to a string
#and display characters 2 and 3

#2-8
print(5+3)


#A list is a collection of items in a particular order. You can make a list that
#includes the letters of the alphabet, the digits from 0–9, or the names of
#all the people in your family. You can put anything you want into a list

# first item in a list to be at position 0, not position 1.
#This is true of most programming languages

cars = [ 'bughati', 'ferrari', 'tesla', 'bmw'] # exersize : 3-3
print(cars [0].title()) # .title makes T capitalized.
print(cars [1])
print (cars [2].title())
print (cars [-1]) # it is special syntax for accessing the last element in the list

message = "My first bicycle was a " + bicycles [0].title() + "."
print(message)

## 3-1
names = ['Nyrkyz', 'Gulnur']
print(names)

##3-2
message = "Hi my friends, are you ready for out first Python class"
print (message)

# the append() method makes easy to buil lists dynamicly
cars =[]
cars.append('s')
cars.append('w')
cars.append('x')
cars.append('y')
print(cars)

#Inserting Elements into a List

cars =['s','w','x','y']
cars.insert(0, 'T')
print(cars)

#Removing Elements from a List

cars =['s','w','x','y']
print(cars)
del cars[0] # using del
print(cars)

#Removing an Item Using the pop() Method
#The pop() method removes the last item in a list
# usefull when list is chronological
cars =['s','w','x','y']
print(cars)
popped_cars = cars.pop()#to show that value is deleted
print(cars)
print(popped_cars) # prove we still have an access to the deleted value

