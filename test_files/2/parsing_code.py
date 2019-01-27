

import os
import re

comment = "gid_does_not_exist"


with open("/Users/gaurish/Documents/Mohit_Brains/Passwd-Parsing/test_files/2/out2.txt", "w") as out_file:
    
    with open("/Users/gaurish/Documents/Mohit_Brains/Passwd-Parsing/test_files/2/passwd", "r") as in_file_99:
        
        for line in in_file_99:
            ki=line.strip()
            if not ki.startswith("#"): ## excluding first few comments in the file "passwd"
                key = line.split(':')
                #print (key[3])
                
                with open("/Users/gaurish/Documents/Mohit_Brains/Passwd-Parsing/test_files/2/group", "r") as in_file_9:

                    for line in in_file_9:
                        
                        li=line.strip()
                        if not li.startswith("#"): ## excluding first few comments in the file "group"
                            
                            lock = line.split(':') 
                            if re.fullmatch( key[3], lock[2] ): ## fullmatch keyword returns True for'1' match with '1' and False for 1' match with '10'

                                out_file.write('{0},{1},{2},{3}' .format(key[0], key[2], key[4], lock[0] + '\n'))
