from flask import Flask, jsonify, request

app = Flask(__name__)


produtos = [
    {"id": 1, "nome": "Celular", "preco": 1800.0},
    {"id": 2, "nome": "Notebook", "preco": 3500.0},
    {"id": 3, "nome": "Computador", "preco": 2500.0}
]


@app.route('/produtos', methods=['GET'])
def adicionar_produto():
    return jsonify(produtos)


@app.route('/produtos', methods=['POST'])
def criar_produto():
  novo_produto = request.get_json()
    
  return jsonify(novo_produto), 201
    
    
if __name__ == '__main__':
    app.run(debug=True)



    
    