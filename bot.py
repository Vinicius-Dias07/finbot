import logging
from telegram.ext import Application
from config import BOT_TOKEN
from database import init_db
from handlers import register_handlers

# Configura o logging antes de tudo — assim qualquer erro de inicialização também é capturado
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Inicializa o banco, monta o bot e começa a escutar mensagens."""
    logger.info("Iniciando o bot...")

    # Garante que a tabela existe antes de qualquer handler ser chamado
    init_db()
    logger.info("Banco de dados pronto.")

    # Cria a aplicação do bot com o token do .env
    app = Application.builder().token(BOT_TOKEN).build()

    # Registra todos os handlers
    register_handlers(app)

    logger.info("Bot rodando! Pressione Ctrl+C para parar.")
    # run_polling fica escutando mensagens em loop até o programa ser interrompido
    app.run_polling()


if __name__ == "__main__":
    main()
