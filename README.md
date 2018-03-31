# Voice Authentication with your phone

Unlock whatever you want with the power of a simple callflow and machine learning.
(project is still under construction)

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) installed

Run in root folder to start a docker container with all the scripts,
```
# docker-compose up --build
```

Login to the container,
```
# docker exec -it tensorflow /bin/bash -c "TERM=$TERM exec bash"
```

Go to /scripts folder
```
To start tensorflow:
# python tf.py 

To start the webserver that listens to the webhook callbacks from Messagebird.
# python server.py
```

To setup the callflow for a number:
Go to www.messagebird.com and get an account and a voice enabled number for the country that you prefer.
Run `python voice_api_requests.py`


# Special regards to SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)