import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL
)
""")

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("cuzcuzeira", 10.0)
)

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("chuteira nike pro max", 2000.0)
)

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("mouse super ruim", 1.0)
)

conexao.commit()
conexao.close()

print("Os produtos foram cadastrado!")
