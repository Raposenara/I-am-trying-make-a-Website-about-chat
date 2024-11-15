from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Mensagem recebida: {msg}')
    send(msg, broadcast=True)

if __name__ == '__main__':
    # Use apenas socketio.run() para evitar conflitos com app.run()
    port = int(os.getenv("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
