import os
import sys
import fileinput

# etc_passwd = input ("Please enter the path for passwd")
# print ("The path is ",etc_passwd)
#
#
# etc_group = input ("Please enter the path for group")
# print  ("The path is",etc_group)
#
# if (etc_passwd) == "/etc/passwd":
#     print ("You entered correct path")
# else:
#     print("Please enter the correct path for passwd again")
#
# if (etc_group) == "/etc/group":
#     print("You entered correct path")
# else:
#     print("Please enter the correct path for group again")

# os.system ("cat /etc/passwd | awk -F':' '{ print $1}' | xargs -n1 groups > user_groups.txt")  #User which groups
# os.system("cat user_groups.txt")

# os.system("cat ./test_files/group | awk -F : '{print $1, $3}' > ./test_files/allgroup.txt")
# os.system("cat ./test_files/passwd | awk -F : '{print $1,$3,$4,$5}' > ./test_files/allusers.txt")

try:
    with open("/Users/mg250074/Documents/pythontest/Passwd-Parsing/test_files/allusers_1.txt", "a") as out_file:

        with open("/Users/mg250074/Documents/pythontest/Passwd-Parsing/test_files/allusers.txt", "r") as in_file:
            for line in in_file:
                new = line + "Z"
                out_file.write(new)

except IOError:
    print ("File not found")

