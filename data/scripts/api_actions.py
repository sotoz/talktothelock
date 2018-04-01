# -*- coding: utf-8 -*-
import requests
import os
import json
mb_url = "https://voice.messagebird.com"
mb_headers = {
    "Authorization": "AccessKey " + os.environ['api_key'],
    "X-MessageBird-Version": "20170314",
    "Content-Type": "application/json; charset=utf-8",
}


def get_recording(call_id, leg_id, recording_id):
    try:
        response = requests.get(
            url=mb_url+"/calls/"+call_id+"/legs/"+leg_id+"/recordings/"+recording_id,
            headers=mb_headers,
        )
        return response.content
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None


def get_recordings(call_id, leg_id):
    try:
        response = requests.get(
            url=mb_url+"/calls/"+call_id+"/legs/"+leg_id+"/recordings/",
            headers=mb_headers,
        )
        return response.content
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None


def get_leg(call_id, leg_id):
    try:
        response = requests.get(
            url=mb_url+"/calls/"+call_id+"/legs/"+leg_id,
            headers=mb_headers,
        )
        return response.content
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None


def get_call(call_id):

    try:
        response = requests.get(
            url=mb_url + "/calls/"+call_id,
            headers=mb_headers,
        )
        return response.content
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None


def create_webhook_request(token, server_url):
    try:
        response = requests.post(
            url=mb_url+"/webhooks",
            headers=mb_headers,
            data=json.dumps({
                "url": ""+server_url+"",
                "token": ""+token+""
            })
        )
        return response.content
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None


def create_callflow_for_number_request(number):
    # Create Call Flow for Number

    try:
        response = requests.post(
            url=mb_url+"/numbers/"+number+"/call-flow",
            headers=mb_headers,
            data=json.dumps({
                "title": "Test",
                "steps": [
                    {
                        "action": "say",
                        "options": {
                            "payload": "ΓΕΙΑ ΣΑΣ. ΠΑΡΑΚΑΛΩ ΠΕΙΤΕ ΤΗΝ ΜΑΓΙΚΗ ΦΡΑΣΗ ΜΕΤΑ ΤΟ ΜΠΗΠ ΚΑΙ ΠΑΤΗΣΤΕ ΕΝΑ ΟΠΟΙΟΔΗΠΟΤΕ ΚΟΥΜΠΙ.",
                            "voice": "female",
                            "language": "el-GR"
                        }
                    },
                    {
                        "action": "record",
                        "options": {
                            "finishOnKey": "any"
                        }
                    }
                ]
            })
        )
        return response.content
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None
