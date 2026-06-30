@app.route("/produtos/<int:id>")
def buscar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)

    return jsonify({"erro": "Não achei o seu produto, volte mais tarde ou entre em contato com nosso suporte."}), 404
