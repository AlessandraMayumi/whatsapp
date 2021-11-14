import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from api.api import api_create_gift
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
    # initialize response
    resp = MessagingResponse()
    response_msg = resp.message()

    # load incoming request
    incoming_msg = request.values.get('Body', '').lower()
    incoming_from = request.values.get('From', '').lower()

    # create a new chat
    chat = db.find_one(filter={'from': incoming_from})
    if not chat:
        response_msg.body(f'HoHoHo, aqui é o Papai Noel, qual é o sei nome?')
        chat = {'status': 1, 'from': incoming_from}
        db.insert([chat])

        return str(resp)

    # find chat or
    status = chat['status']

    if status == 1:
        db.update_one(incoming_from, 'name', incoming_msg, status)
        response_msg.body(f'E, aonde você mora?')

    elif status == 2:
        db.update_one(incoming_from, 'address', incoming_msg, status)
        response_msg.body(f'Qual presente vc gostaria de ganhar do Papai Noel?')

    elif status == 3:
        db.update_one(incoming_from, 'gift', incoming_msg, status)
        chat = db.find_one(filter={'from': incoming_from})
        api_create_gift(chat)
        response_msg.body(f'Continue se comportando e vc pode ganhar uma surpresa. Feliz Natal!!!')
    else:
        db.update_one(incoming_from, 'last_message', incoming_msg, status)
        response_msg.body(f'Estou correndo com a preparação da noite de Natal!')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
