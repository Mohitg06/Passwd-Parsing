import os
import sys

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

os.system ("cat /etc/passwd | awk -F':' '{ print $1}' | xargs -n1 groups > user_groups.txt")
os.system("cat user_groups.txt")
