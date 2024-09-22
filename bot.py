from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import datetime
import settings


logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    update.message.reply_text("Здравствуй, пользователь")


def talk_to_me(update, context):
    text = update.message.text
    # print(text)
    update.message.reply_text(text)


def main():
    my_bot = Updater(
        settings.API_KEY, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot start at " + datetime.date.today().isoformat())
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
