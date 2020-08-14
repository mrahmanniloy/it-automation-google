#!/usr/bin/env python3

import os
import requests
import json

source_dir = "/data/feedback/"

txt_file_list = os.listdir(source_dir)

for f in txt_file_list:
    try:
        feedback_dict = {}
        with open(os.path.join(source_dir, f), 'r') as feedbacks:
            feedback_dict['title'] = feedbacks.readline()
            feedback_dict['name'] = feedbacks.readline()
            feedback_dict['date'] = feedbacks.readline()
            feedback_dict['feedback'] = feedbacks.readline()

            response  = requests.post("http://ip-address/feedback/", json=feedback_dict)
            '''if not response.ok:
                raise Exception("GET failed with status code {}".format(response.status_code))'''
            response.raise_for_status()    
    except FileNotFoundError:
        pass