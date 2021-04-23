# 3/4/2021 String (str) text

fullname = "john doe"

print (fullname)
print(fullname.upper())
print(fullname.lower())
print(fullname.title()) #title() method returns a string where 1st and evry word is upper case
print(fullname.isdigit())
print(f"fullname.isdigit() >> {fullname.isdigit()}")
print(f"fullname.islower() >> {fullname.islower()}")
print(f"fullname.isupper() >> {fullname.isupper()}")

msg = "we are looking at string functions in python."
print(msg.replace('.', '?').title())
print(msg.replace('python', 'java'))
print(msg.replace('.', '?').lower())

# concatination

msg1 = fullname.title() + ", " +msg.title()
print(msg1)
print(fullname.upper() + ", " +msg)

msg = fullname.title() + " " +msg
print(msg)



#working with whitespace and new space

msg2 = fullname.upper() + "\n\t, " +msg
print(msg2)
print(msg2.replace('\t', ''))

msg3 = '\n\t\t\t' + fullname.upper () + ", " +msg
print(msg3)

# str. strip() - removes leading and preceding whitespace

print(msg3 + '!!!')
print(msg3.strip() + '!!!')

# fstring
msg3 = '\n\t\t\t' + fullname.upper () + ", " +msg
msg4 = f"\n\t\t\t{fullname.upper()}, {msg}"
print(msg4)

print("fstring")
last_name = f'brown'
print(last_name)

num = 456
num1 = 600
print(f"num + num1 = {num + num1}")
# print (num.strip()) - strip () is only used for string data type

message = "one of Python's strength is its diverse community."
print(message)

print(f"num / num1 = {num / num1}")
print(f"num * num1 = {num * num1}")
print(f"num / num1 = {num / num1}")
print(f"num * num1 = {num * num1}")

# str(expression) - this will convert the data type or str
print("value of num is: " + str(num))
print("num + num1 = " + str(num + num1))

num3 = "753" # it is a string (str) not integer (int)
print(f"num + num3 = {num + int(num3)}")
 # control + click - will take you where is coming from

num4 = "45.55"
print(f"num + num1 = {float(num4)}")
print (f"num + num3 = int{(num3)}")


# exercise 2-5
#famouse quote i like
quote = ('\t\tNapoleon Hill said,' "\n\t\tOur only limitations are thouse we set up in our minds")
print(quote)