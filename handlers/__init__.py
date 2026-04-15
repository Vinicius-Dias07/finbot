from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from handlers.start import start_handler
from handlers.add import add_handler
from handlers.list import list_handler
from handlers.total import total_handler
from handlers.reset import reset_handler, reset_callback_handler, CALLBACK_CONFIRMAR, CALLBACK_CANCELAR
from handlers.errors import error_handler


def register_handlers(app: Application) -> None:
    """Registra todos os handlers de comando e callback no bot."""
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("add", add_handler))
    app.add_handler(CommandHandler("list", list_handler))
    app.add_handler(CommandHandler("total", total_handler))
    app.add_handler(CommandHandler("reset", reset_handler))

    # CallbackQueryHandler escuta os cliques nos botões inline do /reset
    app.add_handler(CallbackQueryHandler(reset_callback_handler, pattern=f"^({CALLBACK_CONFIRMAR}|{CALLBACK_CANCELAR})$"))

    # Handler de erros — registrado por último, captura tudo que escapou
    app.add_error_handler(error_handler)
