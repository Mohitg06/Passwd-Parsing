'''
# usage of the code can be verified by issuing "python3 parsing.py -h" in the cmd line
# if unable to read any of the input files then IOError is raised
# if content does not match syntax, error is handled using try except
# user input for filepaths in cmd is taken as a string for code operations
# passwd and group file paths are taken as optional arguments by adding prefix '--'
# Function get_json_dump returns required data as a dictionary
# if you want to catch an exception from open, then open has to be wrapped in a try
# lines starting with # are excluded from operation for file parsing
# The strip() method returns a copy of the string with both leading and trailing characters removed
# then each row is divided into a list
# fullmatch keyword returns true for 1:1 and 1:10
# "\n" at the end of every line was taken out from the list of groups
# temp variable keeps track if any group id in the passwd file does not exist in group file
# OrderedDict() maintains the sequence of elements in a row
# all key value pairs for the dict json_dump are dumped in a json file
'''
import sys
import re
import json
from collections import OrderedDict
import argparse
import logging


class Parsing:
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--passwd", help="passwd file path", default="/etc/passwd")
        parser.add_argument("--group", help="group file path", default="/etc/group")

    args = parser.parse_args()
    passwd_file_path = args.passwd
    group_file_path = args.group
    jsonFilePath = "./final_users_with_groups.json"
    logging.basicConfig(filename="logfilename.log", level=logging.INFO)
    logging.basicConfig(filename="logfilename.log", level=logging.ERROR)

    def get_json_dump(passwd_file_path, group_file_path):
        dict_passwd = OrderedDict()
        dict_group = OrderedDict()

        try:
            with open(passwd_file_path, "r") as passwd_file:
                for row_passwd in passwd_file:
                    x = row_passwd.strip()
                    if not x.startswith("#"):
                        passwd_column = x.split(':')
                        if len(passwd_column) < 5:
                            raise Exception("Error: Please enter correct file for passwd file")
                            sys.exit(1)
                        else:
                            key_passwd = passwd_column[0]
                            dict_passwd[key_passwd] = passwd_column[3], passwd_column[2], passwd_column[
                                4]  # group id, uid, full_name
            logging.info("Parsing Password files")

        except IOError:
            logging.error("Error reading passwd file")
            sys.exit(1)

        try:
            with open(group_file_path, "r") as group_file:
                for row_group in group_file:
                    y = row_group.strip()

                    if not y.startswith("#"):
                        group_column = y.split(':')
                        group_column[-1] = group_column[-1].rstrip('\n')
                        if len(group_column) < 2:
                            raise Exception("Error: Please enter correct file for group file")
                            sys.exit(1)
                        else:
                            key_group = group_column[2]
                            dict_group[key_group] = group_column[3:]
            logging.info("Parsing Group files")
        except IOError:
            logging.error("Error: reading group file")
            sys.exit(1)

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
        logging.info("JSON File Created")










