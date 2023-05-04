from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisismysecretkey"
socketio = SocketIO(app, logger=True)

@app.get("/chat/<username>")
def get_chat_page(username):
  return render_template("chat.html", username=username)

@socketio.on("send_message")
def message_received(data):
  emit('message', {'text': data['text'], 'user': data['user']}, broadcast=True)

@app.get("/update_time")
def send_time_update():
  emit('message', {'text': datetime.now(), 'user': 'SERVER'}, broadcast=True)
  
if __name__ == "__main__":
  socketio.run(app, port=5000, debug=True)