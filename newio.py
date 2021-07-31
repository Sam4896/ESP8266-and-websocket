from flask import Flask, render_template
from flask_socketio import SocketIO, send

# setting up the webserver
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefg'
socketio = SocketIO(app, cors_allowed_origins='*',logger=True)


# # adding route
@app.route("/")
def main():
    return render_template("index2.html")

#receive a message from the front end HTML
@socketio.on('message')
def message_recieved(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)
    
if __name__ == "__main__":
    socketio.run(app, host = "0.0.0.0", port= 5000, debug=True)


