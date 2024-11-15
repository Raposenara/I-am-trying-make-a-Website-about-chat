from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

# Criação da aplicação Flask
app = Flask(__name__)

# Definindo uma chave secreta para sessões de cookies (necessário para manter sessões seguras no Flask)
app.config['SECRET_KEY'] = 'minha_chave_secreta'

# Criação da instância do SocketIO para lidar com conexões WebSocket
socketio = SocketIO(app)

# Definindo a rota principal da aplicação
@app.route('/')
def index():
    # Quando o usuário acessa a página inicial, renderiza o template 'index.html'
    return render_template('index.html')

# Definindo o comportamento para mensagens recebidas via WebSocket
@socketio.on('message')
def handle_message(msg):
    # A cada mensagem recebida, a função exibe a mensagem no console
    print(f'Mensagem recebida: {msg}')
    
    # Envia a mensagem recebida para todos os clientes conectados
    send(msg, broadcast=True)

# Iniciando o servidor Flask com SocketIO
if __name__ == '__main__':
    # Obtém a porta de ambiente ou usa 5000 como padrão
    port = int(os.getenv("PORT", 5000))
    
    # Executa o servidor usando socketio.run() para garantir a compatibilidade com WebSockets
    # A configuração 'host="0.0.0.0"' permite que o serviço seja acessado de qualquer endereço IP
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
 