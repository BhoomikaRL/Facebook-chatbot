from flask import Flask,request
from pymessenger import Bot

app = Flask(__name__)
fbAccessToken = "EAAIcQOwVtfsBAKoGAj45liYvei6lUm2MtvvsASz6diYsOJcQnMRxTdhHD6fMZCwury6PCwqHApBHzcgP"

bot = Bot(fbAccessToken)


@app.route('/')
def index():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification failed",403
        return request.args["hub.challenge"],200
    return "HELLO WORLD",200

@app.route('/',methods=['POST'])
def message():
    data = request.get_json()
    #print(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                senderID = messaging_event['sender']['id']
                recipientID = messaging_event['recipient']['id']
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        message = messaging_event['message']['text']
                    else:
                        message = 'No message'
                    response = "You said "+message
                    bot.send_text_message(senderID,response)
    print(message,senderID,recipientID)
    return "hi",200

if __name__ == "__main__":
    app.run(debug=True)
    