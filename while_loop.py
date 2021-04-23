#03/21/2021 while loop, functions
#wile is looping based on condistions

print("** incremsnting the varaible to raech upper boundary**")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("** decrementing the varaible to raech lower boundary**")

current_number = 10
while current_number >= 5:
    print(current_number)
    current_number -= 1
    print(current_number)

print("****game Started*************")
# enter colors,  green - 15 points, yellow - 10, red - 5,
# othe colors or somthing else you loose
# q or quite is to end the game

color = None # used flag
while color !='quite' or color !='q':
    color = input("enter your color(green/yellow/red): ")
    color = color.lower().strip()
    points = 0
    if color =='quite'or color =='q':
        break
    elif color == 'green':
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points == 5
    else:
        print(" sorry, thats not right color. You lost;)")
    print(f"You have {points} point.")
print("closing the game .....")

# 'hello guys'
count = 0
for letter in 'hellow guys':
    if letter == 'l':
        count += 1
print(f"number of l's is :{ count}")
