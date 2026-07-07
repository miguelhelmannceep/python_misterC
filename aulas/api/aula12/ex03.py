from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("tarefas.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def inicializar_banco():
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            feita INTEGER DEFAULT 0
        )
    """)
    conexao.commit()
    conexao.close()

@app.route("/tarefas", methods=["GET"])
def listar():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM tarefas")
    tarefas = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar():
    novo = request.get_json()
    if "titulo" not in novo:
        return jsonify({"erro": "titulo e obrigatorio"}), 400
    
    feita = novo.get("feita", 0) # Se não informado, começa como pendente (0)
    
    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO tarefas (titulo, feita) VALUES (?, ?)",
        (novo["titulo"], feita)
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return jsonify({"id": novo_id, "titulo": novo["titulo"], "feita": feita}), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    if "titulo" not in dados or "feita" not in dados:
        return jsonify({"erro": "titulo e feita sao obrigatorios"}), 400

    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE tarefas SET titulo = ?, feita = ? WHERE id = ?",
        (dados["titulo"], dados["feita"], id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    
    if afetadas == 0:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404
        
    return jsonify({"id": id, **dados})

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def apagar(id):
    conexao = conectar()
    cursor = conexao.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    
    if afetadas == 0:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404
        
    return jsonify({"mensagem": "Tarefa apagada com sucesso"})

if __name__ == "__main__":
    inicializar_banco()
    app.run(debug=True)
