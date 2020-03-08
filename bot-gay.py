import telebot
import config
import random

userList = []
bot = telebot.TeleBot(config.TOKEN)

IDD = -1001435270194

@bot.message_handler(commands=['random'])
def randoms(message):
	i = random.randint(1,27)
	bot.send_message(message.chat.id, str(i))
	
@bot.message_handler(commands=['gay'])
def pidor(message):
	bot.send_message(message.chat.id, "шукаємо підараса, єбать")
	rnd = random.randint(0, len(userList))
	bot.send_message(message.chat.id, "гнида ти їбана, @" + userList[rnd]) 
	
@bot.message_handler(commands=['reg'])
def reg(message):
	userList.append(message.from_user.username)
	bot.send_message(message.chat.id, "Ти зареєстрований :*")


bot.polling(none_stop=True)
# python D:/Telegram/bot.py
