import os
import sys
import getopt
import api_actions

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
            api_actions.create_webhook_request(t,u)
        else:
            print ('No proper server url provided')
            sys.exit(2)
    elif a == 'callflow':
        if n != "":
            api_actions.create_callflow_for_number_request(n)
        else:
            print ('No number provided')
            sys.exit(2)
    else:
        print ('No proper action provided. Options are `webhook` or `callflow`')
        sys.exit(2)


if __name__ == "__main__":
   main(sys.argv[1:])
   