import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS autores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
)
""")

cursor.execute(
    "INSERT INTO autores (nome) VALUES (?)",
    ("Machado de Assis",)
)

cursor.execute(
    "INSERT INTO autores (nome) VALUES (?)",
    ("Monteiro Lobato",)
)

cursor.execute(
    "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
    ("Dom Casmurro", 1)
)

cursor.execute(
    "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
    ("Memórias Póstumas de Brás Cubas", 1)
)

cursor.execute(
    "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
    ("Sítio do Picapau Amarelo", 2)
)

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")
