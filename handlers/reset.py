import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database import reset_expenses

logger = logging.getLogger(__name__)

# Identificadores dos callbacks dos botões inline
CALLBACK_CONFIRMAR = "reset_sim"
CALLBACK_CANCELAR = "reset_nao"


async def reset_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Pergunta ao usuário se realmente quer apagar tudo, usando botões inline."""
    teclado = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🗑️ Sim, apagar tudo", callback_data=CALLBACK_CONFIRMAR),
            InlineKeyboardButton("❌ Cancelar", callback_data=CALLBACK_CANCELAR),
        ]
    ])
    await update.message.reply_text(
        "⚠️ Tem certeza que quer apagar *todos* os seus gastos? Não tem como desfazer!",
        parse_mode="Markdown",
        reply_markup=teclado,
    )


async def reset_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Trata o clique nos botões de confirmação do /reset."""
    query = update.callback_query
    # Precisamos responder o callback para o Telegram parar de mostrar o "carregando"
    await query.answer()

    user_id = update.effective_user.id

    if query.data == CALLBACK_CONFIRMAR:
        try:
            reset_expenses(user_id)
        except Exception:
            logger.exception("Erro ao apagar gastos do banco")
            await query.edit_message_text("⚠️ Algo deu errado. Tente novamente.")
            return

        await query.edit_message_text("🗑️ Todos os seus gastos foram apagados.")

    elif query.data == CALLBACK_CANCELAR:
        await query.edit_message_text("Cancelado. Seus gastos estão safe! 😌")
