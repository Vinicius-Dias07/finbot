# Finance Bot 💰

Bot de organização financeira pessoal para Telegram, feito com Python e SQLite.

## O que ele faz?

| Comando | O que faz |
|---|---|
| `/start` | Boas-vindas e lista de comandos |
| `/add 50 almoço` | Registra um gasto de R$50,00 como "almoço" |
| `/list` | Lista todos os seus gastos |
| `/total` | Mostra o total gasto |
| `/reset` | Apaga tudo (pede confirmação antes) |

## Como rodar

### 1. Crie seu bot no Telegram
1. Abra o Telegram e busque por `@BotFather`
2. Mande `/newbot` e siga as instruções
3. Copie o token gerado

### 2. Configure o ambiente

```bash
# Clone o projeto e entre na pasta
cd finance-bot

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

### 3. Crie o arquivo `.env`

```
BOT_TOKEN=seu_token_aqui
DATABASE_PATH=data.db
```

### 4. Rode o bot

```bash
python bot.py
```

Agora abra o Telegram, encontre seu bot pelo username e mande `/start`.

## Stack

- Python 3.10+
- [python-telegram-bot 20](https://python-telegram-bot.org/) (async)
- SQLite (nativo do Python)
- python-dotenv
