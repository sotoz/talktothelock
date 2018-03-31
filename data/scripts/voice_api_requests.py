import requests
import json
import os
import sys
import getopt

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

def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "ht:n:a:u:", ["webhooktoken=", "number=", "action=", "serverurl="])
    except getopt.GetoptError:
        print ('voice_api_requests.py -h -w -n -a -u')
        sys.exit(2)
    t,n,a,u = '','','',''
    for opt, arg in opts:
        if opt == '-h':
            print ('voice_api_requests.py -w -n -a -u')
            sys.exit()
        elif opt in ("-t", "--webhooktoken"):
            t = arg
        elif opt in ("-n", "--number"):
            n = arg
        elif opt in ("-a", "--action"):
            a = arg
        elif opt in ("-u", "--serverurl"):
            u = arg

    if a == 'webhook':
        if u != "":
            create_webhook_request(t,u)
        else:
            print ('No proper server url provided')
            sys.exit(2)
    elif a == 'callflow':
        if n != "":
            create_callflow_for_number_request(n)
        else:
            print ('No number provided')
            sys.exit(2)
    else:
        print ('No proper action provided. Options are `webhook` or `callflow`')
        sys.exit(2)


if __name__ == "__main__":
   main(sys.argv[1:])
   