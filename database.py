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


def add_expense(user_id: int, amount: float, description: str) -> None:
    """Insere um novo gasto no banco para o usuário."""
    with _connect() as conn:
        conn.execute(
            "INSERT INTO expenses (user_id, amount, description) VALUES (?, ?, ?)",
            (user_id, amount, description),
        )
        conn.commit()


def list_expenses(user_id: int) -> list[Expense]:
    """Retorna todos os gastos do usuário, do mais recente ao mais antigo."""
    with _connect() as conn:
        cursor = conn.execute(
            "SELECT id, user_id, amount, description, created_at "
            "FROM expenses WHERE user_id = ? ORDER BY id DESC",
            (user_id,),
        )
        rows = cursor.fetchall()

    # Converte cada linha do banco em um objeto Expense
    return [Expense(*row) for row in rows]


def get_total(user_id: int) -> tuple[float, int]:
    """Retorna (soma_total, quantidade) de gastos do usuário."""
    with _connect() as conn:
        cursor = conn.execute(
            "SELECT COALESCE(SUM(amount), 0), COUNT(*) FROM expenses WHERE user_id = ?",
            (user_id,),
        )
        total, count = cursor.fetchone()

    return total, count


def reset_expenses(user_id: int) -> None:
    """Apaga todos os gastos do usuário."""
    with _connect() as conn:
        conn.execute("DELETE FROM expenses WHERE user_id = ?", (user_id,))
        conn.commit()
