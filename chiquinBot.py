import os
import telebot
from helpers import search_song
from telebot import types

inMusicConversation = False

token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(token)

# Intents
def search_intent(message):
	content = message.text
	content = content.lower()
	if ('musica' in content) and ('procura' in content):
		return True
	else:
		return False

# Handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, u"Fala meu consagrado!")
# Help
@bot.message_handler(commands=['help'])
def bot_info(message):
	bot.send_message(chat_id=message.chat.id, text='''Fala meu confederado!
Eu me chamo Little Chico, e sou um bot que vai te ajudar a buscar musicas no Spotify!!
Pra pesquisar, só me pede pra procurar uma musica ai ;)''')

# Handling song research
@bot.message_handler(func=search_intent)
def receive_message(message):
		bot.send_message(chat_id=message.chat.id, text="é pra já")
		markup = types.ForceReply(selective=False)
		msg = bot.reply_to(message, u"Qual o nome da musica que você gostaria?", reply_markup=markup)
		bot.register_next_step_handler(msg, get_desired_song)

def get_desired_song(message):
		search = search_song(message.text)
		bot.send_message(chat_id=message.chat.id, text=('Musica: ' + search[0]))
		bot.send_message(chat_id=message.chat.id, text=search[1])

bot.polling()
