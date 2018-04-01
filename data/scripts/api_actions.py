# -*- coding: utf-8 -*-
import requests,os,json


def get_recording(call_id, leg_id, recording_id):
    try:
        response = requests.get(
            url='https://voice.messagebird.com/calls/{callid}/legs/{legid}/recordings/{recordingid}'.format(callid=call_id, legid=leg_id, recordingid=recording_id)
            headers={
                "X-MessageBird-Version": "20170314",
                "Authorization": "AccessKey " + os.environ['api_key'],
                "Content-Type": "application/json",
            })
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    

def create_webhook_request(token, server_url):
    try:
        response = requests.post(
            url="https://voice.messagebird.com/webhooks",
            headers={
                "X-MessageBird-Version": "20170314",
                "Authorization": "AccessKey " + os.environ['api_key'],
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "url": ""+server_url+"",
                "token": ""+token+""
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def create_callflow_for_number_request(number):
    # Create Call Flow for Number

    try:
        response = requests.post(
            url="https://voice.messagebird.com/numbers/"+number+"/call-flow",
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": "AccessKey " + os.environ['api_key'],
                "X-MessageBird-Version": "20170314",
            },
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
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

