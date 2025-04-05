from flask import Flask, jsonify, request

app = Flask(__name__)

# Token estático para autenticação
TOKEN = "seu_token_secreto"

# Middleware para verificar o token
def autenticar_token(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {TOKEN}":
            return jsonify({"erro": "Token inválido ou ausente"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

# Lista de tarefas (exemplo)
tarefas = [{"id": 1, "titulo": "Estudar Flask", "completa": False}]

# Endpoint para listar tarefas (com autenticação)
@app.route('/tarefas', methods=['GET'])
@autenticar_token
def listar_tarefas():
    return jsonify(tarefas)

# Endpoint para adicionar uma nova tarefa (com autenticação)
@app.route('/tarefas', methods=['POST'])
@autenticar_token
def adicionar_tarefa():
    nova_tarefa = request.get_json()

    if not nova_tarefa or 'titulo' not in nova_tarefa or 'completa' not in nova_tarefa:
        return jsonify({"erro": "Dados inválidos. Certifique-se de enviar 'titulo' e 'completa'."}), 400

    nova_tarefa['id'] = max(tarefa['id'] for tarefa in tarefas) + 1 if tarefas else 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

# Endpoint para atualizar uma tarefa pelo ID (com autenticação)
@app.route('/tarefas/<int:id>', methods=['PUT'])
@autenticar_token
def atualizar_tarefa(id):
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    if tarefa:
        dados = request.json
        tarefa.update(dados)
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

# Endpoint para deletar uma tarefa pelo ID (com autenticação)
@app.route('/tarefas/<int:id>', methods=['DELETE'])
@autenticar_token
def deletar_tarefa(id):
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    if tarefa:
        tarefas.remove(tarefa)
        return jsonify({"mensagem": "Tarefa removida com sucesso"}), 200
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)