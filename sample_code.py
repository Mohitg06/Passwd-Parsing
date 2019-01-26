
import os
import re

key = "divya"

with open("/Users/gaurish/Documents/python_practice/sample_90.txt", "w") as out_file:
    with open("/Users/gaurish/Documents/python_practice/sample_99.txt", "r") as in_file_99:
        for line in in_file_99:
            key = line.split()
            
            with open("/Users/gaurish/Documents/python_practice/sample_9.txt", "r") as in_file_9:
                # Loop over each log line
                for line in in_file_9:
                    if re.match(key[3], line):
                        c= line.split()
                        out_file.write('{0} {1}' .format(c[0], c[2] + '\n'))
                        #out_file.close()
                
            

            
        