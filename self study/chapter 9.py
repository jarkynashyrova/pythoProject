# classes
print("-------9-1--------")


class Restaurant:
    def __init__(self, name, type):
        self.name = name.title
        self.type = type

    def describe(self):
        print(f"The Restaurant name : {self.name}")
        print(f"The Cuisine type is : {self.type}")

    def hours(self):
        print(f"The {self.name} is open")


myrest = Restaurant("Cafe De Paris", " Frech Cusince")
myrest.describe()
myrest.hours()

print("-------9-2--Create three different instances from the class, and call "
      "describe_restaurant() for each instance .------")

Thai = Restaurant("Bangock", "Thai Cuisne")  # instance
Thai.describe()
Thai.hours()

print("-------9-3--------")

class User:
    def __init__(self, first, last, race, eye_color):
        self.first = first.title()
        self.last = last.title()
        self.race = race.title()
        self.eye_color = eye_color.title()

    def describe_user(self):
        print("\n" + self.first + " " + self.last)
        print(f" His race: {self.race}")
        print(f" Eye color: {self.eye_color}")

    def greet_user(self):
        print(f"\nPlease wellcome back, {self.first} {self.last}. ")


j = User("Jose", "David", "balck", " hazel")
j.describe_user()
j.greet_user()

print("-------9-4--------")


class Restaurant:
    def __init__(self, name, type):
        self.name = name.title()
        self.type = type
        self.number_served = 0

    def describe(self):
        msg = self.name + " serves wonderful " + self.type
        print("\n" + msg)

    def hours(self):
        print(f"The Restaurant is open")

    def set_number_served(self, number_served):
        self.number_served = self.number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('Cafe De Paris', 'Frech Cusince')
restaurant.describe()

print("\nNumber served: " + str(restaurant.number_served))  # 0

restaurant.number_served = 100
print("Number served: " + str(restaurant.number_served))  # 100

restaurant.increment_number_served(50)
print("Number served: " + str(restaurant.number_served))  # 50

print("-------9-5--------")


class User:
    def __init__(self, first, last, race, eye_color):
        self.first = first.title()
        self.last = last.title()
        self.race = race.title()
        self.eye_color = eye_color.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first + " " + self.last)
        print(f" His race: {self.race}")
        print(f" Eye color: {self.eye_color}")

    def greet_user(self):
        print(f"\nPlease wellcome back, {self.first} {self.last}. ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


j = User("Jose", "David", "balck", " hazel")
j.describe_user()
j.greet_user()

print("\nmaking 3 login attempts")
j.increment_login_attempts()
j.increment_login_attempts()
j.increment_login_attempts()
print(" login attempts: " + str(j.login_attempts))

print("Resetting Login attempts")
j.reset_login_attempts()
print(" login attempts: " + str(j.login_attempts))

print("-------9-6 Inheritance, add an attribute called flavors-------")

class IcecreamStand(Restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ["green tea", "mango", "Vanila"]

    def show_flavors(self):
        print("we have following ice cream in the store: ")
        for flavor in self.flavors:
            print(flavor.title())

ice = IcecreamStand('love', 'Ice cream')
ice.describe()
ice.show_flavors()

print("-------9-7 Inheritance-------")

class Admin(User):

    def __init__(self, first, last, race, eye_color):
        super().__init__(first, last, race, eye_color)
        self.ps = []

    def show_ps(self):
        print("Following are adminstrtive privileges:")
        for p in self.ps:
            print(p.title())

ad = Admin(" Me", "You", "blue", " black")
ad.ps = ["canpost", "candelet", "canadd"]
ad.describe_user()
ad.show_ps()

print("-------9-8 -------")
class Privilages():
    def __init__(self, privileges =[]):
        self.privileges = privileges

    def show_privilages(self):
        print("\nprivilages:")
        if self.privilages:
            for privilege in self.privileges:
                print(" " + privileges)

            else:
                print("this user has no privileges")

ad = Admin(" Me", "You", "blue", " black")
ad.ps = ["canpost", "candelet", "canadd"]
ad.describe_user()
ad.show_ps()

js_privileges = []



