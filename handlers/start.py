from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde ao /start com uma mensagem de boas-vindas."""
    mensagem = (
        "👋 Olá! Eu sou seu bot de finanças pessoais.\n\n"
        "📌 *Comandos disponíveis:*\n"
        "/add <valor> <descrição> — registra um gasto\n"
        "   _Ex: /add 50 almoço_\n\n"
        "/list — lista todos os seus gastos\n"
        "/total — mostra quanto você gastou no total\n"
        "/reset — apaga todos os seus gastos\n\n"
        "Vamos começar? 💪"
    )
    await update.message.reply_text(mensagem, parse_mode="Markdown")
