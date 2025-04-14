from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__, static_folder='public')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@socketio.on('sendMessage')
def handle_message(data):
    print(f"Message: {data}")
    emit('newMessage', data, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print("User connected!")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)