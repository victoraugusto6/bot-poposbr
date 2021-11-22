import telegram
from decouple import config
from telegram.ext import CommandHandler, Updater

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')
DEBUG = config('DEBUG')


def send(msg, chat_id):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=chat_id, text=msg)


def tutoriais(update, context):
    message = f'Olá, {update.message.from_user.first_name}! 😎\n'
    message += '<strong>Segue a lista de tutoriais:</strong>\n\n'

    # Lendo arquivo
    with open('lista-tutoriais.txt', 'r') as file:
        message += file.read()

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, disable_web_page_preview=True,
        parse_mode=telegram.ParseMode.HTML)


def site(update, context):
    message = f'Olá, {update.message.from_user.first_name}! 😎\n'
    message += '<strong>Segue o link do Pop!_OS:\n</strong>'
    message += 'https://pop.system76.com/'

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message, disable_web_page_preview=True,
        parse_mode=telegram.ParseMode.HTML)


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("tutoriais", tutoriais))
    dispatcher.add_handler(CommandHandler("site", site))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    print("Bot em execução.")
    main()
