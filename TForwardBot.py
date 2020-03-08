import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

IDD = -1001435270194

@bot.message_handler(content_types=["text"])
def messages(message):
	bot.forward_message(361567243, message.chat.id, message.message_id)


bot.polling(none_stop=True)
# python D:/Telegram/bot.py
