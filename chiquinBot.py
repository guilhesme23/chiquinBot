import os
import telebot
from googlesearch import search
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

  	if  inMusicConversation == False: 

  		if ("musica" in content) and ("procure" in content):
  			bot.send_message(chat_id=message.chat.id, text="é pra já")
  			bot.reply_to(message, u"Qual o nome da musica que você gostaria?")
  			inMusicConversation = True
  		else:
  			bot.send_message(chat_id=message.chat.id, text=content)
  	else:
  		print("preto")
  		music = "Sua musica é: {}".format(content)
  		bot.send_message(chat_id=message.chat.id, text=music)
  		inMusicConversation = False

bot.polling()
