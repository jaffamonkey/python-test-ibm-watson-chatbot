import watson_developer_cloud
import string
import random
from random import shuffle
import re

# Change the message string before it is sent to Watson API

class ChangeMessageString:


    # Change message string, based lon the type passed to function 
    def changeMessage(message, changeType, swapThis, withThat):
        if changeType == 'lowercaseall':
            messageString = message.lower()
            return messageString
        elif changeType == 'uppercaseall':
            messageString = message.upper()
            return messageString
        elif changeType == 'capitalizefirstletters':
            messageString = message.title()
            return messageString
        elif changeType == 'removeallpunctuation':
            table = str.maketrans({key: None for key in string.punctuation})
            messageString = message.translate(table)
            return messageString
        elif changeType == 'duplicatealletters':
            dup1 = str()  # a new, empty string.
            for char in message:
                dup1 += char + char  # strings concatenate using + and +=
            return(dup1)      
        elif changeType == 'removeallvowels':
            table = str.maketrans(dict.fromkeys('aeiouAEIOU'))
            messageString = message.translate(table)
            # messageString = re.sub(r'[AEIOU]', '', message)
            return messageString
                elif changeType == 'repeatallcharacters':
            n = 3
            messageString = ''.join([char*n for char in message])
            return messageString
        elif changeType == 'duplicatespaces':
            messageString = re.sub('([ ])',r'\1\1', message)
            return messageString
        elif changeType == 'triplespaces':
            messageString = re.sub('([ ])',r'\1\1\1', message)
            return messageString
        elif changeType == 'shufflelettersretainspaces':
            words = []
            for word in message.split():
                if len(word) > 1:
                    words.append(word[0]
                            + ''.join(random.sample(
                                [char for char in word[1:-1]], len(word) - 2))
                            + word[-1])
                else:
                    words.append(word)
            result = ' '.join(words)
        elif changeType == 'swapletters':
            messageString = swapletters(message, swapThis, withThat)
            return messageString
        else 
            return message

    def swapLetters(message, swapThis, withThat):
        messageString = message.replace(swapThis, withThat)
        return messageString


    def garble_word(match):
        first, middle, last = match.groups()
        middle = list(middle)
        shuffle(middle)
        return first + ''.join(middle) + last


    def garble(sentence):
        return RE_GARBLE.sub(garble_word, sentence)