import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Captura qualquer exceção não tratada e responde ao usuário com uma mensagem amigável."""
    # Loga o traceback completo — essencial para debugar depois
    logger.exception("Erro não tratado no update %s", update, exc_info=context.error)

    # Tenta avisar o usuário se o update veio de uma mensagem normal
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "⚠️ Algo deu errado por aqui. Tente novamente mais tarde."
        )
