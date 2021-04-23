# 03/21/2021 Functions increase your reuseability

def greet_user():
    """this is a docstring, something that describe the function."""
    print("Hello!!!")


def greet_user_by_name(name):
    """
    it will say hello and use the name entered.
    name is required parameter, user has to pass to a function
    """
    print(f"Hello, {name.title()}!")
    print(f"Hi, Mrs/Mr {lastname.title()}!")

def sum_numbers(num1, num2):
    print(f"sum of {num1} and {num2} is {num2 + num1}")
    print(f"square of the {num2} is : {num2 ** 2}")


# def describe_pet(pet='dog', pet_name ): always put required parameters first
def describe_pet(pet_name, pet='dog'):
    """
    Keyword argument is pet with default value
    :param pet_name:
    :param pet: it is pet type : dog, cat etc, optional param, default is dog
    :return:
    """
    print(f"I have a {pet} and we call it {pet_name.title()}")


#  ******************************************************
# All executions of the functions (Calling the functions)
greet_user()  # this is how you CALL function
# greet_user_by_name()  # expected TypeError
# greet_user_by_name('ali')
sum_numbers(45, 78)
sum_numbers(-46, 34)
sum_numbers(num2=-46, num1=34)

describe_pet('Lazy', 'cat')
describe_pet('Fluffy', 'dog')
describe_pet('Fluffy')
describe_pet(pet='cat', pet_name='Pretty')
# describe_pet(pet='snake')  # TypeError: required parameter is missing


def favorite_book(book_title):
    print(f"one of my favorite books is '{book_title.upper()}'....")

def test_function(part1: str):
    print(f"hello{part1.lower()} ")

favorite_book("sun aslo rises")

def multi_num(a: int, b: int): # in python we dont have to mention data type but in java and c sharp you have to mention
    c = a * b
    print(f"product of {a} and {b} is {c}, ")

multi_num(5, 6)
multi_num(5.555, 6)
multi_num(True, True)
multi_num(False, True)
# multi_num('a', 'b')typeerror: all errors are negative test cases done
# multi_num(4.5)
# multi_num(3, 5, .10) error
# multi_num('@','#')
# multi_num(\n,\t)

#a.exercises for problem solving:
#1. How to swap 2 variable values. e.g.: a=45 b=78 >> a=78 b=45
print("\n---------swap-----------")
a = 45
b = 78
print(" the value  a :{}", format(a))
print(" the value  a :{}", format(b))

def swap(a,b):
    print(f"the value of a is:{a}")
    print(f"the value of b is:{b}")

swap(45, 89)


# swapping the values without using a variable
print("___________________________________")
num1 = 'number one'
num2 = 'number two'
print(num1,"---",  num2)
num1, num2 = num2, num1
print(num1,"---",  num2)