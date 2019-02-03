

import os
import sys
import fileinput
import re
import json
import csv


class Parsing:

    out_group = ("./out_group.txt")
    jsonFilePath = ("./final_users_with_groups.json")
    data = {}
    with open(out_group , "w") as out_file:
        out_file.write("username;uid;full_name;groups\n")

        with open("/etc/passwd", "r") as passwd_file:
            for row_passwd in passwd_file:
                ki = row_passwd.strip()

                if not ki.startswith("#"):  ## excluding first few comments in the file "passwd"
                    key = row_passwd.split(':')

                    with open("/etc/group", "r") as group_file:
                        temp = 0

                        for row_group in group_file:
                            li = row_group.strip()

                            if not li.startswith(
                                    "#"):  ## excluding first few comments in the file "group"
                                lock = li.split(':')

                                _uid = {"uid": key[2]}
                                _fullname = {"full_name": key[4]}
                                _groups = {"groups": lock[3:]}

                                if re.fullmatch(key[3], lock[
                                    2]):  ## fullmatch keyword returns True for'1' match with '1' and False for 1' match with '10'
                                    out_file.write('{0};{1};{2};{3}\n'.format(key[0], _uid, _fullname,
                                                                              _groups))  ## username, uid, fullname, groups
                                    temp = +1  # temp variable incremented when when fullmatch found

                        if temp == 0:  # at the end of parsing group file, if temp variable equates to zero, that means error condition
                            out_file.write(
                                '{0};{1};{2};ERROR: no info found for group id {3}\n'.format(list(key[0]), _uid,
                                                                                             _fullname,
                                                                                             _groups))  ## username, uid, fullname, error message

    with open(out_group) as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=';')

        for csvRow in csvReader:
            username = csvRow["username"]  # initialize item to be parsed as a key
            data[username] = csvRow['uid'], csvRow['full_name'], csvRow['groups']

    with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))



