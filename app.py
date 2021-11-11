import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from db.conn import DatabaseService

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG,
                    format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')


@app.route("/", methods=['GET'])
def hello():
    app.logger.info('Hello, World, test')
    return "Hello, World!"


@app.route("/", methods=['POST'])
def reply():
    db = DatabaseService()
    db.insert(request.json)

    incoming_msg = request.values.get('Body', '').lower()

    resp = MessagingResponse()
    response_msg = resp.message()
    response_msg.body(f'this is the response text "{incoming_msg}"')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
