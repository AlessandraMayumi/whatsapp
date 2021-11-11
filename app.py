import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from sandbox.send import send_one_way_message

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')


@app.route("/", methods=['GET'])
def hello():
    app.logger.info('Hello, World, test')
    return "Hello, World!"


@app.route("/", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.json
    app.logger.info(msg)
    # Create reply
    resp = MessagingResponse()
    resp.message("From Python, you said: {}".format(msg))

    return '', 200


if __name__ == "__main__":
    app.run(debug=True)
