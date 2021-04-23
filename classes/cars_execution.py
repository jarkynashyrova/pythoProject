# 4/3/2021
# this  file is for executing the cars.py classes
from classes.cars import Car,ElectricCar # import more than one class just do *

mycar = Car("BMW", "530xi", "black") # parameters
yourcar = Car("lexus","lexus IS", "silver")

print("==============================")
mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.set_odometer_reader(25)
mycar.set_odometer_reader(60)
mycar.__odo_reader = 20
mycar.color = 'RED'
mycar.get_description()

print("++++++++++++++++++++++++++++++")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()

# 04/03/2021
print("-----------Electric Car instances__________________")

my_ev = ElectricCar("tesla", 'model x', 'blue')
my_ev.drive()
my_ev.get_description()
# child is not depended from parent when you createing attributes
print('\nBattery Size: ' , my_ev.battery_size)
#mycar.battery_size # only child has betry size
#Car( state,behavior) -> ElectricCar(state, behavior)

# we can create new method(functions, available to child only)
my_ev.get_battery_infor()

# we can get override(what parent had) the method that had (000ps -methid Override)
my_ev.get_description()

mycar.drive()
my_ev.drive()