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

# Get all workspace ids and put into an array
        
class GetAllWorkspaceIds:
    
    def getWorkspaceIds():
        username = config['DEFAULT']['watson_username']
        password = config['DEFAULT']['watson_password']
        version = config['DEFAULT']['watson_version']
        url = config['DEFAULT']['watson_url']
        assistant = \
                watson_developer_cloud.AssistantV1(username=username,password=password,version=version,url=url)
        response = assistant.list_workspaces().get_result()
        data = json.dumps(response)
        data2 = json.loads(data)
        workspaces=[]
        for p in data2['workspaces']:
            workspaces.append(p['workspace_id'])
        print(workspaces)
        return workspaces