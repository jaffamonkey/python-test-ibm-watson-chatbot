#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import watson_developer_cloud
import os
import time
import configparser
from logger import Logger
from watson_developer_cloud import WatsonApiException
from changemessage import ChangeMessageString
from getallmessages import GetMessagesForAllIntents

config = configparser.ConfigParser()
config.read('config.conf')


# Send messages, using the message files stored "input" directory

class SendMessages:

    def __init__(self, changemessage):
        self.changemessage = changemessage

    def sendMessages(self):
        username = config['DEFAULT']['watson_username']
        password = config['DEFAULT']['watson_password']
        version = config['DEFAULT']['watson_version']
        url = config['DEFAULT']['watson_url']
        space_id = os.environ.get('SPACE_ID')
        directory = './input/' + space_id + '/'
        time.sleep(5)
        if space_id == None:
            exit("Missing environment variable: SPACE_ID")
        if not os.path.exists('logs/'):
            os.makedirs('logs')    
        if not os.path.exists('report'):
            os.makedirs('report') 
        
        # Loop round each filename in directory
        
        for filename in os.listdir(directory):
            intent = os.path.splitext(filename)[0]
            f = open('report/' + space_id + '/' + self.changemessage + '-' + intent
                     + '.json', 'a+')
            flog = open('logs/' + space_id + '/' + self.changemessage + '-' + intent
                        + '.log', 'a+')
            fsummary = open('report/' + space_id + '/' + self.changemessage
                            + 'summary-results.txt', 'a+')

            # Open file and read line by line

            with open(directory + filename) as fp:
                line = fp.readline()
                cnt = -1
                totalpass = 0

                # Set watson developer cloud credentials

                assistant = \
                    watson_developer_cloud.AssistantV1(username=username,
                        password=password, version=version, url=url)

                # Execute send message, using each line as message to send

                while line:
                    time.sleep(0.5)
                    try:
                        line = \
                        ChangeMessageString.changeMessage(fp.readline(),
                            self.changemessage)
                        # Execute message post

                        assistant.set_detailed_response(True)

                        # Send message to the specified workspace

                        response = \
                            assistant.message(workspace_id=space_id
                                , page_limit=1000,
                                input={'text': line.strip()}).get_result()
                        resp = json.dumps(response).count('intent": "'
                                + intent + '"')

                        # Return pass/failresult for matching intent

                        if resp == 1:
                            Logger.log_pass(response)
                            f.write(json.dumps(response) + ',\n')
                            totalpass += \
                                json.dumps(response).count('intent": "'
                                + intent + '"')
                            # resp_dict = json.loads(response)
                            # resp_dict['intents']
                            # confidence = resp_dict['confidence']
                            # print('Confidence level: ' + confidence)
                            cnt += 1
                        else:
                            Logger.log_fail(response)
                            f.write(json.dumps(response) + ',\n')
                            # flog.write(json.dumps(response) + ',\n')
                            cnt += 1
                    except requests.exceptions.ConnectionError as ex:

                    # Write request exseptions to log file

                        Logger.log_fail(str(ex))
                        flog.write(str(ex) + ',\n')

                     # Write Watson API exceptions to log file

                    except WatsonApiException as err:
                        Logger.log_fail(str(err))
                        flog.write(str(err) + ',\n')
                summaryline = 'total with correct intent(' + intent \
                    + '): ' + str(totalpass) + ' from total messages: ' \
                    + str(cnt) + '\n'
                # print(summaryline)

                # Write summaries of passed tests to report summary file

                fsummary.write(summaryline)
            f.close()
            flog.close()
            fsummary.close()


# if __name__== "__main__":
#   main()s

GetMessagesForAllIntents.getMessagesForAllIntents()
SendMessages('baseline').sendMessages()
SendMessages('duplicatespaces').sendMessages()
SendMessages('triplespaces').sendMessages()
SendMessages('duplicatealletters').sendMessages()
SendMessages('lowercaseall').sendMessages()
SendMessages('uppercaseall').sendMessages()
SendMessages('capitalizefirstletters').sendMessages()
SendMessages('removeallpunctuation').sendMessages()
SendMessages('removeallvowels').sendMessages()
SendMessages('shufflelettersretainspaces').sendMessages()
SendMessages('swapdwiths').sendMessages()
SendMessages('swapawiths').sendMessages()