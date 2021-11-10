from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from sandbox.send import send_one_way_message

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "Hello, World!"


@app.route("/", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.json

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    send_one_way_message()
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
