'''
# usage of the code can be verified by issuing "python3 new_5.py -h" in the cmd line
# output json file is written in year_month_day_hour_min_sec format inside ./LOGS/OUTPUT folder
# os.path.dirname(path) Returns the directory name of pathname path.
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
# exit(0) means a clean exit without any errors / problems
# exit(1) means there was some issue / error / problem and that is why the program is exiting.
# This is useful for other programs, shell, caller etc. to know what happened with your program and proceed accordingly.
'''

import time
import sys
import os
import re
import json
from collections import OrderedDict
import argparse
import logging

class Parse():

    def __init__(self):
        self.logger=logging.getLogger(__name__)
        self.timestr = "output_" + time.strftime("%Y_%m_%d_%H_%M_%S")
        self.jsonFile = "./LOGS/OUTPUT/{}.json".format(self.timestr)
        self.jsonFileDirectory = os.path.dirname(self.jsonFile)

        self.hdlr = logging.FileHandler('./LOGS/logging.log')
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(logging.INFO)

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--passwd", help="passwd file path", default="/etc/passwd")
        self.parser.add_argument("--group", help="group file path", default="/etc/group")

        self.args = self.parser.parse_args()
        self.passwd_file_path = self.args.passwd
        self.group_file_path = self.args.group


    def path(self):
        if not os.path.exists(self.jsonFileDirectory):
            try:
                os.makedirs(self.jsonFileDirectory)
            except OSError as e:
                raise Exception('Error: Permission denied to create output directory at {}'.format(self.jsonFile))


    def get_json_dump(self,passwd_file_path, group_file_path):

        dict_passwd = OrderedDict()
        dict_group = OrderedDict()

        try:
            with open(passwd_file_path, "r") as passwd_file:
                for row_passwd in passwd_file:
                    x = row_passwd.strip()
                    if not x.startswith("#"):
                        passwd_column = x.split(':')
                        if len(passwd_column) < 5:
                            raise Exception(
                                "Error: Content of the passwd file does not follow correct syntax. Please enter correct passwd file")
                        else:
                            key_passwd = passwd_column[0]
                            dict_passwd[key_passwd] = passwd_column[3], passwd_column[2], passwd_column[
                                4]  # group id, uid, full_name
        except IsADirectoryError as err:
            self.logger.error("Error: Program cannot read Directory, please enter coorect passwd file")
        except PermissionError as err:
            self.logger.error("Error: Program does not have permission to read passwd file, please check permissions")
        except IOError as err:
            self.logger.error("I/O Error: Program failed to access passwd file")
        except:
            self.logger.error("Error: Unexpected error accessing passwd file")
            sys.exit(1)

        try:
            with open(group_file_path, "r") as group_file:
                for row_group in group_file:
                    y = row_group.strip()
                    if not y.startswith("#"):
                        group_column = y.split(':')
                        group_column[-1] = group_column[-1].rstrip('\n')
                        if len(group_column) < 2:
                            raise Exception(
                                "Error: Content of the passwd file does not follow correct syntax. Please enter correct group file")
                        else:
                            key_group = group_column[2]
                            dict_group[key_group] = group_column[3:]
        except IsADirectoryError as err:
            self.logger.error("Error: Program cannot read Directory, please enter coorect group file", exc_info=True)
        except PermissionError as err:
            self.logger.error("Error: Program does not have permission to read group file, please check permissions",
                         exc_info=True)
        except IOError as err:
            self.logger.error("I/O Error: Program failed to access group file", exc_info=True)
        except:
            self.logger.error("Error: Unexpected error accessing group file",
                         exc_info=True)  # change print statment to consider above raise exception
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


    def json_print(self):
        try:
            with open(self.jsonFile, "w") as f:
                json.dump(self.get_json_dump(self.passwd_file_path, self.group_file_path), f, indent=4)
                self.logger.info('{} file created'.format(self.jsonFile))

        except PermissionError as err:
            print(
                "Error: Program does not have permission to write output json file {}, please check permissions".format(
                    self.jsonFile))

        except:
            print("Error: Unexpected error accessing group file")





json_print=Parse()
json_print.json_print()








