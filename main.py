from telegram import Game, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

TOKEN = '7514272138:AAG3r5s1lVPRlDv2WgPLBuKPJOl5iLx1_mk'  # Замените на ваш токен
WEBSITE_URL = 'https://github.com/YComeDY/curly-enigma.git'  # Ваш URL веб-приложения

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Начать игру", web_app=WebAppInfo(url=WEBSITE_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("*Добро пожаловать в CS MINE!*", reply_markup=reply_markup, parse_mode='Markdown')

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Обработка нажатия кнопки (вы можете добавить свой функционал)
    await update.callback_query.answer("Кнопка нажата!")

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавление обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))

    # Запускаем бота
    app.run_polling()

if __name__ == "__main__":
    main()
