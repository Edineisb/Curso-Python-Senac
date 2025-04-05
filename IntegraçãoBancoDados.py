import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


DATABASE = 'tarefas.db'

def init_db():
    """Inicializa o banco de dados e cria a tabela de tarefas, se não existir."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                completa BOOLEAN NOT NULL
            )
        ''')
        conn.commit()


init_db()


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas')
        tarefas = [
            {"id": row[0], "titulo": row[1], "completa": bool(row[2])}
            for row in cursor.fetchall()
        ]
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.get_json()

    if not nova_tarefa or 'titulo' not in nova_tarefa or 'completa' not in nova_tarefa:
        return jsonify({"erro": "Dados inválidos. Certifique-se de enviar 'titulo' e 'completa'."}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tarefas (titulo, completa) VALUES (?, ?)',
            (nova_tarefa['titulo'], nova_tarefa['completa'])
        )
        conn.commit()
        nova_tarefa['id'] = cursor.lastrowid

    return jsonify(nova_tarefa), 201


@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados_atualizados = request.get_json()

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
        tarefa = cursor.fetchone()

        if not tarefa:
            return jsonify({"erro": "Tarefa não encontrada"}), 404

        cursor.execute(
            'UPDATE tarefas SET titulo = ?, completa = ? WHERE id = ?',
            (dados_atualizados.get('titulo', tarefa[1]),
             dados_atualizados.get('completa', tarefa[2]),
             id)
        )
        conn.commit()

    return jsonify({"id": id, "titulo": dados_atualizados.get('titulo', tarefa[1]), "completa": dados_atualizados.get('completa', tarefa[2])})


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
        tarefa = cursor.fetchone()

        if not tarefa:
            return jsonify({"erro": "Tarefa não encontrada"}), 404

        cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
        conn.commit()

    return jsonify({"mensagem": "Tarefa removida com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)