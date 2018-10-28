#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os

# Send messages, using the message files stored "input" directory


class ExtractWordsMatchingCount:

    def extractWordsMatchingCount(count):
        space_id = os.environ.get('SPACE_ID')
        directory = './input/' + space_id + '/'

        # Loop round each filename in directory
        for filename in os.listdir(directory):
            space_count = 0
            f2 = open(directory + count + '.txt', 'a+') 
            intent = os.path.splitext(filename)[0]
            lines = filename.readlines()
            for line in lines:
                space_count = line.count('')
                if space_count == count - 1:
                    f.write(line + ',' + intent + ',' + space_id)
                    f.close()

# if __name__== "__main__":
#   main()s

ExtractSingleWordExamples.extractWordsMatchingCount(2)
