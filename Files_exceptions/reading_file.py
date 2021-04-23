#04/04/2021 Rading a file
##filepath = "\\Users/jashyrova08gmailcom/dev/Basics/Data/student.txt" for windows ||
filepath = "/Users/jashyrova08gmailcom/dev/Basics/Data/students.txt" # absolute path

##============== Reading from a File==========
# with open(filepath) as students: # opens the file and saves in the memory
#     contents = students.read()
#     print(contents)
#
# with open(filepath) as students:
#     for line in students:
#         print(line, end =' ')
## making a list of lines from a File
# with open(filepath,'r') as students: # 'r' is an optional parameter for mode, r
#is default mode  that opens in READ ONLY mode
#     lines=students.readlines()
#
# print(lines)
# print(lines[0].strip())
# print(lines[7])
# print("=================")
# for line in lines:
#     print(line)

##============== Reading from a File==========
with open(filepath,'a') as students: # 'a' is for append so sergey is added to the file content.
# 'w'is for write, thats truncate the file and adds new content.
    print("WRITING TO THE FILE..")
    students.write("\nSERGEY")


with open(filepath,'r') as students:
    lines=students.readlines()
    print(lines)

print("Program is completed")