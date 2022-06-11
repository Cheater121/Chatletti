from flask import Flask, request, render_template

app = Flask(__name__)
list_of_messages = []


@app.route("/")
def start_page():
    return render_template('index.html')


# sending messages to server
@app.route("/api/messenger", methods=['POST'])
def sendmessage():
    msg = request.json
    if (len(msg)) == 3 and "Username" in msg.keys() and "Timestamp" in msg.keys() and "Messagetext" in msg:
        list_of_messages.append(msg)
        return "Success! Received messages: 1.", 200
    else:
        return "Wrong format", 200


@app.route("/api/messenger/<int:i>")
def getmessage(i):
    if 0 <= i < len(list_of_messages):
        return list_of_messages[i], 200
    else:
        return "Not found", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
