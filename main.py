from flask import Flask, request

app = Flask(__name__)
list_of_messages = []
list_of_messages.append({"Username": "Test",
                         "Messagetext": "test",
                         "Timestamp": "2022-06-05S16:23:10.1123456"})


@app.route("/")
def hello_world():
    return "Hello World!"


# checking status (how many messages received)
@app.route("/status")
def status():
    return {
        "Total messages": len(list_of_messages)
    }


# sending messages to server
@app.route("/api/messenger", methods=['POST'])
def sendmessage():
    msg = request.json
    print(msg)
    list_of_messages.append(msg)
    msg_text = f"{msg['Username']} <{msg['Timestamp']}>: {msg['Messagetext']}"
    print(f"Total messages: {len(list_of_messages)} Last received message: {msg_text}")
    return f"Success! Total messages: {len(list_of_messages)}", 200


@app.route("/api/messenger/<int:i>")
def getmessage(i):
    print(i)
    if 0 <= i < len(list_of_messages):
        print(list_of_messages[i])
        return list_of_messages[i], 200
    else:
        return "Not found", 400


if __name__ == '__main__':
    app.run()