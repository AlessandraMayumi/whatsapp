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
    # initialize response
    resp = MessagingResponse()
    response_msg = resp.message()

    # load incoming request
    incoming_msg = request.values.get('Body', '').lower()
    incoming_from = request.values.get('From', '').lower()

    # find chat or create a new one
    chat = db.find_one(filter={'from': incoming_from})
    if not chat:
        chat = {'status': 1, 'from': incoming_from, 'name': incoming_msg}
        db.insert([chat])
        response_msg.body(f'HoHoHo, aqui é o Papai Noel, qual é o sei nome?')
        return str(resp)

    status = chat['status']

    if status == 1:
        response_msg.body(f'E, aonde você mora?')
        db.update_one(incoming_from, 'address', incoming_msg, status)

    elif status == 2:
        response_msg.body(f'Qual presente vc gostaria de ganhar do Papai Noel?')
        db.update_one(incoming_from, 'gift', incoming_msg, status)

    elif status == 3:
        response_msg.body(f'Continue se comportando e vc pode ganhar uma surpresa. Feliz Natal!!!')
        db.update_one(incoming_from, 'last_message', incoming_msg, status)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
