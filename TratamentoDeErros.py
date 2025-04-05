from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de exemplo
tarefas = [{"id": 1, "titulo": "Estudar Flask", "completa": False}]

# Tratamento de erro 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"erro": "Recurso não encontrado"}), 404

# Tratamento de erro 400 - Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"erro": "Requisição inválida"}), 400

# Endpoint para listar tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

# Endpoint para adicionar uma nova tarefa
@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.get_json()

    if not nova_tarefa or 'titulo' not in nova_tarefa or 'completa' not in nova_tarefa:
        return jsonify({"erro": "Dados inválidos. Certifique-se de enviar 'titulo' e 'completa'."}), 400

    nova_tarefa['id'] = max(tarefa['id'] for tarefa in tarefas) + 1 if tarefas else 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

# Endpoint para buscar uma tarefa pelo ID
@app.route('/tarefas/<int:id>', methods=['GET'])
def buscar_tarefa(id):
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify(tarefa)

if __name__ == '__main__':
    app.run(debug=True)