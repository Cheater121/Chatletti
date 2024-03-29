from flask import Flask, request, render_template, url_for
from tests import msg_validator

app = Flask(__name__)
dict_of_messages = {}


@app.route("/")
def start_page():
    return render_template('index.html')


# getting messages by server from user
@app.route("/api/messenger", methods=['POST'])
def getmessage():
    msg = request.json
    if msg_validator(msg):
        recipient = msg.pop("Recipient")
        if recipient not in dict_of_messages:
            dict_of_messages[recipient] = [msg]
        else:
            dict_of_messages[recipient].append(msg)
        return "Success! Received messages: 1.", 200
    else:
        return "Wrong format", 400


# sending messages to user from server
@app.route("/api/messenger/<username>")
def sendmessage(username):
    try:
        if len(dict_of_messages[username]) > 0:
            messages = dict_of_messages.get(username)
            answer = {username: messages}
            dict_of_messages[username] = []
            return answer, 200
        elif len(dict_of_messages[username]) == 0:
            return "Not found", 200
    except KeyError:
        return "Not found user", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
