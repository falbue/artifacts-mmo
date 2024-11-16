from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.API_TG)  # создание бота

def tg_notif(text):
	bot.send_message(config.TG_USER, text)