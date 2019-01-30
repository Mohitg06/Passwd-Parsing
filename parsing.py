import os
import sys
import fileinput
import re
import json
import csv
#
#
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
#
# os.system ("cat /etc/passwd | awk -F':' '{ print $1}' | xargs -n1 groups > user_groups.txt")  #User which groups
# os.system("cat user_groups.txt")
#
# os.system("cat ./group.txt | awk -F : '{print $1, $3}' > ./test_files/allgroup.txt")
# os.system("cat ./test_files/passwd | awk -F : '{print $1,$3,$4,$5}' > ./test_files/allusers.txt")

# try:
#     with open("/Users/mg250074/Documents/pythontest/Passwd-Parsing/test_files/allusers_4.txt", "a") as out_file:
#
#         with open("/Users/mg250074/Documents/pythontest/Passwd-Parsing/test_files/allusers.txt", "r") as in_file:
#             for line in in_file:
#                 out_file.write(line.rstrip('\n') + string_to_add + '\n')
#
# except IOError:
# #     print ("File not found")

import os
import re

with open("./test_files/2/out5.txt", "w") as out_file:
    with open("./test_files/2/passwd", "r") as in_file_99:

        for line in in_file_99:
            ki = line.strip()
            if not ki.startswith("#"):  ## excluding first few comments in the file "passwd"
                key = line.split(':')

                with open("./test_files/2/group", "r") as in_file_9:
                    temp = 0
                    for line in in_file_9:

                        li = line.strip()
                        if not li.startswith("#"):  ## excluding first few comments in the file "group"

                            lock = line.split(':')
                            if re.fullmatch(key[3], lock[
                                2]):  ## fullmatch keyword returns True for'1' match with '1' and False for 1' match with '10'
                                temp = +1
                                out_file.write(
                                    '"username": {0},"uid": {1},"full_name": {2},"groups": {3}'.format(key[0], key[2],
                                                                                                       key[4], lock[3]))
                    if temp == 0:
                        out_file.write(
                            '"username": {0},"uid": {1},"full_name": {2},ERROR: no info found for group id {3}\n'.format(
                                key[0], key[2], key[4], key[3]))

sys.stdout = open('output.json', 'w')
with open('./test_files/2/out5.txt', 'r') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    i = 0
    header = []
    out_data = []
    for row in filereader:
        row = [elem for elem in row if elem]
        if i == 0:
            i += 1
            header = row
        else:
            row[0:2] = [row[0]+" "+row[1]]
            _dict = {}
            for elem, header_elem in zip(row, header):
                _dict[header_elem] = elem
            out_data.append(_dict)

print (json.dumps(out_data))


