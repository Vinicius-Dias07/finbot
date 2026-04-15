from dataclasses import dataclass


@dataclass
class Expense:
    """Representa um gasto registrado pelo usuário."""
    id: int
    user_id: int
    amount: float
    description: str
    created_at: str
