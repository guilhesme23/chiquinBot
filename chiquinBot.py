import os
import telebot

token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, u"Fala meu consagrado!")

@bot.message_handler(func=lambda message: True)
def shout_message(message):
  	content = message.text
  	if content == "procure uma musica":
  		bot.send_message(chat_id=message.chat.id, text="é pra já")
  		bot.reply_to(message, u"Qual o nome da musica que você gostaria?")
  	else:
  		bot.send_message(chat_id=message.chat.id, text=content)
bot.polling()
