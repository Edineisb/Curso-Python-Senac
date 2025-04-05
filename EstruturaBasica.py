from flask import Flask, jsonify, request


app = Flask(__name__)

tarefas = [{"id": 1, "titulo": "Estudar Flask", "completa": False}]


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.get_json()

    if not nova_tarefa or 'titulo' not in nova_tarefa or 'completa' not in nova_tarefa:
        return jsonify({"erro": "Dados inválidos. Certifique-se de enviar 'titulo' e 'completa'."}), 400

    nova_tarefa['id'] = max(tarefa['id'] for tarefa in tarefas) + 1 if tarefas else 1

    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    if tarefa:
        dados = request.json
        tarefa.update(dados)
        return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = next((t for t in tarefas if t['id'] == id), None)
    if tarefa:
        tarefas.remove(tarefa)
        return jsonify({"mensagem": "Tarefa removida com sucesso"}), 200
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
    
      


    

