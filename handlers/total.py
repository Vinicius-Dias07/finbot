import logging
from telegram import Update
from telegram.ext import ContextTypes
from database import get_total

logger = logging.getLogger(__name__)


async def total_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra a soma total dos gastos do usuário."""
    user_id = update.effective_user.id

    try:
        total, quantidade = get_total(user_id)
    except Exception:
        logger.exception("Erro ao calcular total de gastos")
        await update.message.reply_text("⚠️ Algo deu errado. Tente novamente.")
        return

    if quantidade == 0:
        await update.message.reply_text("📭 Nenhum gasto registrado ainda.")
        return

    await update.message.reply_text(
        f"💰 Total: R${total:.2f} em {quantidade} gasto{'s' if quantidade > 1 else ''}"
    )
