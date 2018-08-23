import os
import telebot
from helpers import search_song

inMusicConversation = False

token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, u"Fala meu consagrado!")

@bot.message_handler(func=lambda message: True)
def shout_message(message):
  	content = message.text
  	global inMusicConversation

  	if  not inMusicConversation: 

  		if ("musica" in content) and ("procure" in content):
  			bot.send_message(chat_id=message.chat.id, text="é pra já")
  			bot.reply_to(message, u"Qual o nome da musica que você gostaria?")
  			inMusicConversation = True
  		else:
  			bot.send_message(chat_id=message.chat.id, text=content)
  	else:
  		search = search_song(content)
  		bot.send_message(chat_id=message.chat.id, text=('Musica: ' + search[0]))
  		bot.send_message(chat_id=message.chat.id, text=search[1])
  		inMusicConversation = False

bot.polling()
