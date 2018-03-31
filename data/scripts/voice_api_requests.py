import requests
import json
import os
import sys
import getopt

def create_webhook_request():
    try:
        response = requests.post(
            url="https://voice.messagebird.com/webhooks",
            headers={
                "X-MessageBird-Version": "20170314",
                "Authorization": "AccessKey " + os.environ['api_key'],
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "url": ""+os.environ['server_url']+"",
                "token": "foobar1234"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def create_callflow_for_number_request():
    # Create Call Flow for Number

    try:
        response = requests.post(
            url="https://voice.messagebird.com/numbers/"+os.environ['phone_number']+"/call-flow",
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
            argv, "hc:n:a:", ["callflow=", "number=", "action="])
    except getopt.GetoptError:
        print ('voice_api_requests.py -h -a -c -n')
        sys.exit(2)
    c,n,a = '','',''
    for opt, arg in opts:
        if opt == '-h':
            print ('voice_api_requests -a -c -w -n')
            sys.exit()
        elif opt in ("-c", "--callflow"):
            c = arg
        elif opt in ("-n", "--number"):
            n = arg
        elif opt in ("-a", "--action"):
            a = arg

    if a == 'webhook':
        create_webhook_request()
    elif a == 'callflow':
        create_callflow_for_number_request()
    else:
        print ('No proper action provided. Options are `webhook` or `callflow`')
        sys.exit(2)


if __name__ == "__main__":
   main(sys.argv[1:])
   