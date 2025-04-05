
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    concluida = db.Column(db.Boolean, default=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'concluida': self.concluida,
            'data_criacao': self.data_criacao.strftime('%Y-%m-%d %H:%M:%S')
        }

# Criar tabelas no banco de dados
with app.app_context():
    db.create_all()

# GET /tarefas: Retorna todas as tarefas
@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    tarefas = Tarefa.query.all()
    return jsonify([tarefa.to_dict() for tarefa in tarefas])

# POST /tarefas: Adiciona uma nova tarefa
@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    dados = request.get_json()
    
    if not dados or 'titulo' not in dados:
        return jsonify({'erro': 'Dados inválidos. O título é obrigatório'}), 400
    
    nova_tarefa = Tarefa(
        titulo=dados['titulo'],
        descricao=dados.get('descricao', ''),
        concluida=dados.get('concluida', False)
    )
    
    db.session.add(nova_tarefa)
    db.session.commit()
    
    return jsonify(nova_tarefa.to_dict()), 201

# PUT /tarefas/int:id: Atualiza uma tarefa pelo id
@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get(id)
    
    if not tarefa:
        return jsonify({'erro': f'Tarefa com id {id} não encontrada'}), 404
    
    dados = request.get_json()
    
    if 'titulo' in dados:
        tarefa.titulo = dados['titulo']
    if 'descricao' in dados:
        tarefa.descricao = dados['descricao']
    if 'concluida' in dados:
        tarefa.concluida = dados['concluida']
    
    db.session.commit()
    
    return jsonify(tarefa.to_dict())

# DELETE /tarefas/int:id: Remove uma tarefa pelo id
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def remover_tarefa(id):
    tarefa = Tarefa.query.get(id)
    
    if not tarefa:
        return jsonify({'erro': f'Tarefa com id {id} não encontrada'}), 404
    
    db.session.delete(tarefa)
    db.session.commit()
    
    return jsonify({'mensagem': f'Tarefa com id {id} removida com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
