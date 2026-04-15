import sqlite3
from config import DATABASE_PATH
from models import Expense


def _connect() -> sqlite3.Connection:
    """Abre e retorna uma conexão com o banco SQLite."""
    return sqlite3.connect(DATABASE_PATH)


def init_db() -> None:
    """Cria a tabela de gastos se ela ainda não existir."""
    with _connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                amount      REAL    NOT NULL,
                description TEXT    NOT NULL,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now', 'localtime'))
            )
        """)
        conn.commit()
