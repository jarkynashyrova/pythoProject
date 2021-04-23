#03/28/2021 object oriented Programming Concepts: Class and Object
# class name starts always upper case example :Car(optional) (it means function) is good, car is not good

class Car:# class name is Car with upper case
    """This class describes model of the car."""
    def __init__(self, brand, model, color):# __init___ is a contructer function colled
        """this is the contstructor, with required parameters"""
        self.model = model # assighning the local brand variable to
         # a global variable (self.model is global)
        self.color = color
        self.brand = brand # attributes
        self.__odo_reader = 0 #encapsulation- hiding data from

    def set_odometer_reader(self, miles): #set updated, creates the odometer
        """Function to update the value of the self odo_reader global variable"""
        #if miles > self.odo_reader:
        if miles > self.__odo_reader:
            self.__odo_reader = miles
        else:
            print("miles can not be less than odometer miles")

    def drive(self): # parameter,
        """driving action"""
        print(f"you are driving the car without DL! is isn't it "
              f"awsome!")
        if self.brand.lower() == "bmw":
            print(f" you are driving FAST car even without DL! isnt it awsome")

        else:
            print(f"awsome")

    def do_somthing(self):
        print(f"I want to do somthing ")
        print(f"let me drive this car;)")
        self.drive()
        #motor =  motorcycle()
        #motor.drive()

    def get_description(self):
        """ this is constrction, with required"""
        print(f"model of the car : {self.model}")
        print(f"color of the car : {self.color}")
        print(f"brand of the car : {self.brand}")
        print(f" you have {self.__odo_reader} miles on your car.")

class ElectricCar(Car):
    """This is the child class of Car. Electric class inherits from Car class"""

    def __init__(self, brand, model, color, battery_size = 60):# __init___ is a contructer function colled
        """this is the contstructor, with required parameters""" #battery_size = 60 is optional
        super().__init__(brand, model, color)
        self.battery_size = battery_size

    def get_battery_infor(self):
        print(f"This car has {self.battery_size} KWh battery.")

    def get_description(self):
        super().get_description()
        print(f"battery size of the car: {self.battery_size}")

    def drive(self):
        print("you are driving EV! it is way awsome than just a car, maybe")