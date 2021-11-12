# Noel chat

https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio

### Sign in Whatsapp
- add Twilio Sandbox
> +1 (415) 523-8886

- send message
> join use-danger

### Noel chat
 
> oi

> HoHoHo, aqui é o Papai Noel, qual é o sei nome?
 
> Enzo

> E, aonde você mora?

> Rua Bartholomeu, 47

> Qual presente vc gostaria de ganhar do Papai Noel?

> carrinho

### Schema

```
{
    "_id": {
        "$oid": "618ef8ebd232d004eb1ce19a"
    },
    "status": {
        "$numberInt": "4"
    },
    "from": "whatsapp: 5519989711675",
    "name": "oi",
    "address": "enzo",
    "gift": "rua bartholomeu de gusmão, 47",
    "last_message": "tetris"
}
```

### State Machine

The chat is identified through the sender phone number and each new message from the same number is incremented the 
field status 0 to the first message until 3 to the ending message.
