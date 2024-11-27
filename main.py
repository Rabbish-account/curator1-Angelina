import telebot

bot = telebot.TeleBot('7330593282:AAGHRds2aPRfLJV9RHYPmR6m3550g8Wf1fk')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello', parse_mode='Markdown')


bot.infinity_polling()


@bot.message_handler(commands=['good bot'])
def main(message):
    bot.send_message(message.chat.id, 'Thanks', parse_mode='Markdown')


bot.infinity_polling()


@bot.message_handler(commands=['bad bot'])
def main(message):
    bot.send_message(message.chat.id, 'I am offended', parse_mode='Markdown')


bot.infinity_polling()


@bot.message_handler(commands=['I like pizza'])
def main(message):
    bot.send_message(message.chat.id, 'Me too', parse_mode='Markdown')


bot.infinity_polling()


@bot.message_handler(commands=['I like cola'])
def main(message):
    bot.send_message(message.chat.id, 'Me too', parse_mode='Markdown')


bot.infinity_polling()

