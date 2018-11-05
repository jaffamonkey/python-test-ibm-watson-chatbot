#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import watson_developer_cloud
import requests
import os
import shutil
import configparser
from logger import Logger
from getallintents import GetAllIntents
from watson_developer_cloud import WatsonApiException

config = configparser.ConfigParser()
config.read('config.conf')


# Get examples directly from Watson API, and populate input files

class GetMessagesForAllIntents:
    
    # Loops through intents and retirives all examples, processed by intent

    def getMessagesForAllIntents():
        space_id = os.environ.get('SPACE_ID')
        username=config['DEFAULT']['watson_username']
        password=config['DEFAULT']['watson_password']
        version=config['DEFAULT']['watson_version']
        url=config['DEFAULT']['watson_url']
        intents = GetAllIntents.getAllIntents()
        
        if not os.path.exists('input'):
            os.makedirs('input')
        if not os.path.exists('logs'):
            os.makedirs('logs')
        if not os.path.exists('input/' + space_id):
            os.makedirs('input/' + space_id) 

        # Start of message sending loop
        
        for intent in intents:
            
            # Set watson credentials and url

            assistant = \
                watson_developer_cloud.AssistantV1(username=username,password=password,version=version,url=url)
            
            # Retrieve examples using Waston Python SDK 
            
            flog = open('logs/importmessages-' + intent + '.log', 'w+')
            try:
                assistant.set_detailed_response(True)
                response2 = \
                    assistant.list_examples(workspace_id=space_id
                        , intent=intent, page_limit=1000).get_result()
                flog.write(json.dumps(response2) + ',\n')

            # Catch error and output to screen

            except requests.exceptions.ConnectionError as ex:
                Logger.log_fail(str(ex))
                flog.write(str(ex) + ',\n')
            except WatsonApiException as err:
                Logger.log_fail(str(err))
                flog.write(str(err) + ',\n')

            # Create new examples file for intent

            f = open('input/' + space_id + '/' + intent + '.txt', 'w+')

            # Clean returned data

            messages = \
                json.dumps(response2).replace('{"examples": [{"text": "'
                    , '').replace('"}, {"text": "', '\n').split('"',
                    1)[0].replace('@country', 'Nederland').replace(
                    '@country', 'Nederland').replace(
                    '@brand', 'Sony').replace(
                    '@phone:accessories', 'kabel').replace(
                    '@phone', 'iphone').replace(
                    '@family', 'family').replace(
                    '@sys-number', '1').replace(
                    '@guarantee', 'garantie').replace('@provider', 'Lebara')
                    
            # Write messages to input file
            
            f.write(messages)
        f.close()