#03/13/2021 chapter 4
# working with part of the list
cars = ['bugatti','ferrai', 'tesla', 'lexus']

# slice of the list list_name[start:stop]
#start is inclusive, stop is exclusive value
# value: list_name[start, list list_name [start +1], ......[stop-1]
for car in cars[1:3]: # using range of index 1-3
    print(f"the car is : {car}")

print("----------second---------------")
for car in cars[:3]: # same thing as cars as cars [0-3}
    print(f"the car is : {car}")

print("----------thirtd--------------")
for car in cars[2:]: # the same thing as cars [2:end of thelist]
    print(f"the car is : {car}")

print("----------fourth--------------")
for car in cars[2:10]: # no index out of range error
    print(f"the car is : {car}")

print("----------copying and linking--------------")
print("----------linking the 2 variable to the same value--------------")
cars2 = cars
print(f"the car is : {car}")
print(f"the car2 is : {cars2}")
cars.append('bmw')
print(f"the car is : {car}")
print(f"the car2 is : {cars2}")

print("----------copying--------------")
cars3 = cars [:]
#del cars[2]
print(f"cars")
print(f"cars")
print(f"the car is : {car}")
print(f"the car2 is : {cars2}")

print(" --------4-10----------")
print(f"The fisrt three items in the list are:{cars[:3]}")
print(f"The three items from the middle of the list are:{cars[2:5]}")
print(f"The last three items in the list are:{cars[3:]}")

print("-------Tuples----------")
# lists can be  modified (mutable)
#Tuples - (immutable) data structure similar to the list but can not be-
# -modified ( you cant change or update)
cars_t = ('bugatti','ferrai', 'tesla', 'lexus')
print(f"fisrt value is : {cars_t[0]}")
cars [0] = 'honda' # this is possible since cars is the list data structure
#cars_t[0] = 'honda' # this is not possible since the cars _t is tuple d/s
print(f"cars _t :{cars_t}")

cars_t = ('honda','ferrari','tesla') # override
print(f"cars_t tuple:{cars_t}")