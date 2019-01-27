

import os
import re

with open("/Users/gaurish/Documents/Mohit_Brains/Passwd-Parsing/test_files/2/out5.txt", "w") as out_file:
    
    with open("/Users/gaurish/Documents/Mohit_Brains/Passwd-Parsing/test_files/2/passwd", "r") as in_file_99:
        
        for line in in_file_99:
            ki=line.strip()
            if not ki.startswith("#"): ## excluding first few comments in the file "passwd"
                key = line.split(':')
                
                with open("/Users/gaurish/Documents/Mohit_Brains/Passwd-Parsing/test_files/2/group", "r") as in_file_9:
                    temp = 0 ## temp variable to check error condition
                    
                    for line in in_file_9:
                        
                        li=line.strip()
                        if not li.startswith("#"): ## excluding first few comments in the file "group"
                            
                            lock = line.split(':') 
                            if re.fullmatch( key[3], lock[2] ): ## fullmatch keyword returns True for'1' match with '1' and False for 1' match with '10'
                                temp =+1
                                out_file.write('"username": {0},"uid": {1},"full_name": {2},"groups": {3}' .format(key[0], key[2], key[4], lock[3] ))
                    
                    if temp == 0: ## error condition satisfied
                        out_file.write('"username": {0},"uid": {1},"full_name": {2},ERROR: no info found for group id {3}\n' .format(key[0], key[2], key[4], key[3]))
