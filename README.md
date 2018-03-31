# Voice Authentication with your phone

Unlock whatever you want with the power of a simple callflow and machine learning.
(project is still under construction)

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) installed

Run in root folder,
~~~~
docker-compose build && docker-compose up -d
~~~~

Login to the container,
~~~~
docker exec -it tensorflow /bin/bash -c "TERM=$TERM exec bash"
~~~~

Go to /scripts folder and run
~~~~
python tf.py
~~~~

# Special regards to SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)