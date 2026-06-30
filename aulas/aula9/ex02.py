from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Camiseta Chad", "preco": 500.0}
]

@app.route("/produtos", methods=["GET"])
def listar():
    return jsonify(produtos)

# POST com validação
@app.route("/produtos", methods=["POST"])
def criar():
    novo = request.get_json()

    if "preco" not in novo:
        return jsonify({"erro": "O preco eh obrigatorio"}), 400

    produtos.append(novo)
    return jsonify(novo), 201

app.run(debug=True)
