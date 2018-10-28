        #!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import watson_developer_cloud
import os
import configparser
from logger import Logger
from watson_developer_cloud import WatsonApiException


config = configparser.ConfigParser()
config.read('config.conf')

# Get all intents for a workspace and put into an array
        
class GetAllIntents:
    
    def getAllIntents():
        username = config['DEFAULT']['watson_username']
        password = config['DEFAULT']['watson_password']
        version = config['DEFAULT']['watson_version']
        url = config['DEFAULT']['watson_url']
        space_id = os.environ.get('SPACE_ID')

        # Set watson credentials and url
        
        assistant = \
            watson_developer_cloud.AssistantV1(username=username,password=password,version=version,url=url)
        response = assistant.list_intents(workspace_id = space_id).get_result()
        data = json.dumps(response)
        data2 = json.loads(data)
        intents=[]
        for i in data2['intents']:
            intents.append(i['intent'])
        print(intents)
        return intents