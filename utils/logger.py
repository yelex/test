import telebot
# from telebot import apihelper

from constants import TOKEN

# apihelper.proxy = {'http':'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

bot.send_message(chat_id='yellex', text="Choose one letter:")
# bot.infinity_polling()