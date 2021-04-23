#03/26/2021 imporing the modules
# import you do anywhere


#import time
#import from anywhere
from time import *
import sys
from functions.functions_return import *


#from functions.functions_return import *

# import functions.functions_return as ft
#functions.functions_returnprint_formatted_name("akmal",'husanov')
sleep(5) # use this 'from time import

print(sys.platform)
#print_formatted_name("akmal","husanov") #if  import *
#ft.print_formatted_name("akmal","husanov") #if as FT
#time.sleep(5) # if you used 'import time'


full_name = get_formatted_name('john', 'doe')
print(full_name)
print(get_formatted_name('jane', 'doe'))

print_formatted_name('ali', 'tehrani')
student = print_formatted_name('baur', 'eskara')
print(f"value of student is : {student}")
print(f"value of student is : {print_formatted_name('baur', 'eskara')}")