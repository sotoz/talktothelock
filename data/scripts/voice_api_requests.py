import requests
import json
import os


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
            url="https://voice.messagebird.com/numbers/"+os.environ['phone_number']"/call-flow",
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


if __name__ == '__main__':
    from sys import argv
    try:
        opts, args = getopt.getopt(
            argv, "hcw:n:", ["attach_callflow=", "number="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-c", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

create_callflow_for_number_request()
