# exception handling - handle the situations where you expect certain type of error
# when you predict somthing going to be wrong

filepath = "/Users/jashyrova08gmailcom/dev/Basics/Data1/students.txt"


try:
    print("trying block started")
    with open(filepath,'a') as students:
        print("WRITING TO THE FILE..")
        students.write("\nSERGEY")

    with open(filepath,'r') as students:
        lines=students.readlines()
        print(lines)

except FileNotFoundError as err:
    print(err)
    print("enter correct file path.check your file path.")


# print(5/0)
try:
    num= 5/int(input('enter the number to divide by:'))
    print("enter correct file path.check your file path.")
    print(f"Result of this division: {num}")
except ZeroDivisionError as err:
    print("you can not divide by zero")
else:# this is dependant on try block, if try block executes else block will be executed
    print("this is else block)")
finally:
    print('I am a Fianally bloack, I am always executed whatever happens with try, except or block')
