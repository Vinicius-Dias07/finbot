import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Lê o token do bot — se não existir, para tudo com mensagem clara
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN não encontrado. Crie o arquivo .env com seu token.")

# Caminho do banco de dados SQLite (padrão: data.db na raiz do projeto)
DATABASE_PATH = os.getenv("DATABASE_PATH", "data.db")
