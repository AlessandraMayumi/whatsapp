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
    chat = db.find_one(filter={'From': incoming_from})
    if not chat:
        chat = {'status': 0, 'from': incoming_from}
        db.insert(chat)

    status = chat['status']
    chat.status += 1

    # conditional response
    if not status:
        response_msg.body(f'HoHoHo, aqui é o Papai Noel, qual é o sei nome?')

    elif status == 1:
        response_msg.body(f'E, aonde você mora?')
        db.update_one({"From": incoming_from}, {"$set": {"name": incoming_msg}})

    elif status == 2:
        response_msg.body(f'Qual presente vc gostaria de ganhar do Papai Noel?')
        db.update_one({"From": incoming_from}, {"$set": {"gift": incoming_msg}})

    elif status == 3:
        response_msg.body(f'Continue se comportando e vc pode ganhar uma surpresa. Feliz Natal!!!')
        db.update_one({"From": incoming_from}, {"$set": {"last_message": incoming_msg}})

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
