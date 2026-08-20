import sqlite3

DB_NAME = "banco.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def carregar_notas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title AS titulo, content AS detalhes, id AS id
        FROM note
    """)

    notas = cursor.fetchall()
    conn.close()
    return notas

def adicionar_notas(titulo, detalhes):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO note (title, content) VALUES (?, ?)",
        (titulo, detalhes)
    )

    conn.commit()
    conn.close()

def deletar_notas(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM note WHERE id = ?",
        (id, )
    )

    conn.commit()
    conn.close()

def carregar_nota(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title AS titulo, content AS detalhes FROM note WHERE id = ?",
        (id, )
    )

    note = cursor.fetchone()
    conn.close()
    return note

def atualizar_nota(id, title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE note SET title = ?, content = ? WHERE id = ?",
        (title, content, id)
    )

    conn.commit()
    conn.close()