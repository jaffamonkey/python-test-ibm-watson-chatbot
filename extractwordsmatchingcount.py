#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os

class ExtractExamplesBasedOnWordCount:

    def extractExamplesBasedOnWordCount(numberWords):
        space_id = os.environ.get('SPACE_ID')
        directory = './input/' + space_id + '/'

        # Loop round each filename in directory
        for filename in os.listdir(directory):
            space_count = 0
            intent = os.path.splitext(filename)[0]
            with open(directory + filename, 'r') as file:
                for line in file:  
                    print(line)
                    f = open(directory + numberWords + '.txt', 'a+') 
                    space_count = line.count(' ')
                    print(space_count)
                    if space_count == numberWords-1:
                        f.write(line)
                        f.close()

# if __name__== "__main__":
#   main()s

ExtractExamplesBasedOnWordCount(1)
