from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Mouse ruim", "preco": 10.90, "disponivel": True},
    {"id": 2, "nome": "Mouse médio", "preco": 50.90, "disponivel": True},
    {"id": 3, "nome": "Mouse bom", "preco": 200.90, "disponivel": False},
    {"id": 4, "nome": "Mouse muito bom", "preco": 3500.90, "disponivel": True}
]

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)
