import logging
from telegram import Update
from telegram.ext import ContextTypes
from database import add_expense

logger = logging.getLogger(__name__)


async def add_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Registra um novo gasto. Uso: /add <valor> <descrição>"""
    # context.args contém os argumentos depois do comando, separados por espaço
    # Ex: /add 50 almoço  →  context.args = ['50', 'almoço']
    if not context.args or len(context.args) < 2:
        await update.message.reply_text(
            "❌ Formato inválido. Use: /add <valor> <descrição>\n"
            "_Ex: /add 50 almoço_",
            parse_mode="Markdown",
        )
        return

    valor_str = context.args[0]
    descricao = " ".join(context.args[1:])  # une o restante caso tenha espaços

    # Tenta converter o valor para número — se não conseguir, avisa o usuário
    try:
        valor = float(valor_str.replace(",", "."))  # aceita vírgula ou ponto
    except ValueError:
        await update.message.reply_text(
            "❌ Valor inválido. Use um número. Ex: /add 50 almoço"
        )
        return

    if valor <= 0:
        await update.message.reply_text("❌ O valor precisa ser maior que zero.")
        return

    user_id = update.effective_user.id

    try:
        add_expense(user_id, valor, descricao)
    except Exception:
        logger.exception("Erro ao salvar gasto no banco")
        await update.message.reply_text("⚠️ Algo deu errado. Tente novamente.")
        return

    await update.message.reply_text(
        f'✅ R${valor:.2f} registrado como "{descricao}"'
    )
