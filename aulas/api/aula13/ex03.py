from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("biblioteca.db")
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route("/autores/<int:autor_id>/livros", methods=["GET"])
def livros_autor(autor_id):

    conexao = conectar()

    cursor = conexao.execute(
        "SELECT * FROM livros WHERE autor_id = ?",
        (autor_id,)
    )

    livros = [dict(livro) for livro in cursor.fetchall()]

    conexao.close()

    return jsonify(livros)


@app.route("/livros/busca", methods=["GET"])
def buscar():

    titulo = request.args.get("titulo")

    conexao = conectar()

    cursor = conexao.execute(
        "SELECT * FROM livros WHERE titulo LIKE ?",
        (f"%{titulo}%",)
    )

    livros = [dict(livro) for livro in cursor.fetchall()]

    conexao.close()

    return jsonify(livros)

if __name__ == "__main__":
    app.run(debug=True)
