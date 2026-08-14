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
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            details TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def carregar_notas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title AS titulo, details AS detalhes
        FROM notas
    """)

    notas = cursor.fetchall()
    conn.close()
    return notas

def adicionar_notas(titulo, detalhes):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO notas (title, details) VALUES (?, ?)",
        (titulo, detalhes)
    )

    conn.commit()
    conn.close()