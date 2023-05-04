import os
import telebot 

API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Welcome to Argha Bot!')
	bot.send_message(message.chat.id, "Say hello to me just by tapping on \n\n/hello command")
	

@bot.message_handler(commands=['hello'])
def hello(message):
	bot.send_message(message.chat.id, "Hey, Argha Bot this side! How it's going?\n\nExplore my portfolio\nhttp://t.me/HelloArgha_bot/HelloArgha")
	
bot.polling()