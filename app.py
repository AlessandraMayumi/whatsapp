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

    chat = [{'From': incoming_from, 'To': incoming_to, 'Body': incoming_msg, 'MessageSid': incoming_msid}]
    db.insert(chat)

    resp = MessagingResponse()
    response_msg = resp.message()

    if incoming_msg == 'oi':
        response_msg.body(f'HoHoHo aqui é o Papai Noel, qual é o sei nome?')

    elif 'nome' in incoming_msg.lower():
        response_msg.body(f'E, aonde você mora?')

    elif 'rua' in incoming_msg.lower() or 'ave' in incoming_msg.lower():
        response_msg.body(f'Qual presente vc gostaria de ganhar do Papai Noel?')
    else:
        response_msg.body(f'Feliz Natal')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
