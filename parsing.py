'''
# Function get_json_dump returns required data as a dictionary
# lines starting with # are excluded from operation for file parsing
# The strip() method returns a copy of the string with both leading and trailing characters removed
# then each row is divided into a list
# fullmatch keyword returns true for 1:1 and 1:10
# "\n" at the end of every line was taken out from the list of groups
# temp variable keeps track if any group id in the passwd file does not exist in group file
# OrderedDict() maintains the sequence of elements in a row
# all key value pairs for the dict json_dump are dumped in a json file
'''

import re
import json
import sys
from collections import OrderedDict

class Parsing:

    passwd_file_path=(sys.argv[1])
    group_file_path = (sys.argv[2])
    jsonFilePath = "./final_users_with_groups.json"

    if passwd_file_path != "/etc/passwd":
        print ("Enter right file path for passwd")
        sys.exit (0)

    if group_file_path != "/etc/group":
        print ("Enter right file path for groups")
        sys.exit (0)

    def get_json_dump(passwd_file_path, group_file_path):
        dict_passwd = OrderedDict()
        dict_group = OrderedDict()

        with open(passwd_file_path, "r") as passwd_file:
            for row_passwd in passwd_file:
                x = row_passwd.strip()
                if not x.startswith("#"):
                    passwd_column = x.split(':')
                    key_passwd = passwd_column[0]
                    dict_passwd[key_passwd] = passwd_column[3], passwd_column[2], passwd_column[
                        4]  # group id, uid, full_name

        with open(group_file_path, "r") as group_file:
            for row_group in group_file:
                y = row_group.strip()

                if not y.startswith("#"):
                    group_column = y.split(':')
                    group_column[-1] = group_column[-1].rstrip('\n')
                    key_group = group_column[2]
                    dict_group[key_group] = group_column[3:]

        json_dump = OrderedDict()

        for key_passwd, value_passwd in dict_passwd.items():
            temp = 0
            for key_group, value_group in dict_group.items():
                if re.fullmatch(value_passwd[0], key_group):
                    temp = temp + 1
                    obj = OrderedDict()
                    obj["uid"] = value_passwd[1]
                    obj["full_name"] = value_passwd[2]
                    obj["group"] = value_group
                    json_dump[key_passwd] = obj
            if temp == 0:
                obj = OrderedDict()
                obj["uid"] = value_passwd[1]
                obj["full_name"] = value_passwd[2]
                obj["group"] = "Error: Info does not exist"
                json_dump[key_passwd] = obj

        return OrderedDict(json_dump)

    with open(jsonFilePath, "w") as f:
        json.dump(get_json_dump(passwd_file_path, group_file_path), f, indent=4)







