import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from db.conn import DatabaseService

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG,
                    format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')

db = DatabaseService()


@app.route("/", methods=['GET'])
def hello():
    app.logger.info('Hello, World, test')
    return "Hello, World!"


@app.route("/", methods=['POST'])
def reply():
    incoming_msg = request.values.get('Body', '').lower()
    incoming_from = request.values.get('From', '').lower()
    incoming_to = request.values.get('To', '').lower()
    incoming_msid = request.values.get('MessageSid', '').lower()

    chat = [{'body': incoming_msg, 'From': incoming_from, 'To': incoming_to, 'MessageSid': incoming_msid}]
    app.logger.info(chat)
    db.insert(chat)

    resp = MessagingResponse()
    response_msg = resp.message()
    response_msg.body(f'this is the response text "{incoming_msg}"')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
