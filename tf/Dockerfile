FROM tensorflow/tensorflow:latest-py3

EXPOSE 8000
ENV api_key=set_your_messagebird.com_api_key_here
ENV server_url=your_server_that_has_the_webhooks
ENV phone_number=the_number_you_have_at_messagebird

RUN pip install requests

RUN mkdir /scripts
