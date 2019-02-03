import os
import sys
import fileinput

import re
import json
import csv


class Parsing():
    def __init__(self):
        self.file_name = ("out8.csv")
        self.path = ("./test_files/2/")
        self.full_path = os.path.join(self.path,self.file_name)
        self.file_name_open = open (self.full_path, "w")



    def file_open(self):
        # self.path = open("./test_files/2/out8.csv", "w")

        with self.file_name_open  as out_file:
            with open("/etc/passwd", "r") as in_file_99:

                out_file.write("username,uid,full_name,groups\n")
                for line in in_file_99:
                    ki = line.strip()
                    if not ki.startswith("#"):  ## excluding first few comments in the file "passwd"
                        key = line.split(':')

                        with open("/etc/group", "r") as in_file_9:
                            temp = 0
                            for line in in_file_9:

                                li = line.strip()
                                if not li.startswith("#"):  ## excluding first few comments in the file "group"

                                    lock = line.split(':')
                                    if re.fullmatch(key[3], lock[
                                        2]):  ## fullmatch keyword returns True for'1' match with '1' and False for 1' match with '10'
                                        temp = +1
                                    out_file.write(
                                    '{0},{1},{2},{3}'.format(key[0], key[2], key[4], lock[3]))
                            if temp == 0:
                                out_file.write(
                                '{0},{1},{2},ERROR: no info found for group id {3}\n'.format(key[0], key[2], key[4],
                                                                                             key[3]))

        return self.file_name_open

# csvFilePath = ("./test_files/2/out8.csv")
# jsonFilePath = ("./test_files/2/out8.json")
#
# data = {}
#
# with open(csvFilePath) as csvFile:
#     csvReader = csv.DictReader(csvFile)
#
#     for csvRow in csvReader:
#         username = csvRow["username"]
#         data[username] = csvRow


# with open(jsonFilePath, "w") as jsonFile:
#     jsonFile.write(json.dumps(data))
