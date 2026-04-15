import logging
from telegram import Update
from telegram.ext import ContextTypes
from database import list_expenses

logger = logging.getLogger(__name__)


async def list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Lista todos os gastos do usuário."""
    user_id = update.effective_user.id

    try:
        gastos = list_expenses(user_id)
    except Exception:
        logger.exception("Erro ao buscar lista de gastos")
        await update.message.reply_text("⚠️ Algo deu errado. Tente novamente.")
        return

    if not gastos:
        await update.message.reply_text("📭 Nenhum gasto registrado ainda.")
        return

    linhas = ["📋 *Seus gastos:*\n"]
    for gasto in gastos:
        # Formata cada linha como: • R$50,00 — almoço (2024-01-15 12:30:00)
        linhas.append(
            f"• R${gasto.amount:.2f} — {gasto.description} _{gasto.created_at}_"
        )

    await update.message.reply_text("\n".join(linhas), parse_mode="Markdown")
