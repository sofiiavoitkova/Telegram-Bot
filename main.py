import telebot
import logging
from credentials import bot_token, bot_user_name

bot = telebot.TeleBot(bot_token)
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = f"Welcome to {bot_user_name}! \n\nReady to explore? Click on the menu to begin!"
    bot.send_message(message.chat.id, welcome_message, reply_markup=create_menu_keyboard())


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    warning_message = "Please use the provided menu to interact with the bot."
    bot.send_message(message.chat.id, warning_message)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(query):
    if query.data == "show_menu":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_us = telebot.types.InlineKeyboardButton(text="US", callback_data="us")
        button_eu = telebot.types.InlineKeyboardButton(text="EU", callback_data="eu")
        keyboard.add(button_us, button_eu)

        bot.send_message(query.message.chat.id, "Please select a region:", reply_markup=keyboard)
    elif query.data == "us":
        bot.send_photo(query.message.chat.id,
                       open('graphs/US.jpg', 'rb'))
        bot.send_photo(query.message.chat.id,
                       open('graphs/TUS.jpg', 'rb'))
        bot.send_message(query.message.chat.id, "You selected US. Would you like to make another selection? "
                                                "\n\nClick on the menu to choose again!",
                         reply_markup=create_menu_keyboard())
    elif query.data == "eu":
        bot.send_photo(query.message.chat.id,
                       open('graphs/EU.jpg', 'rb'))
        bot.send_photo(query.message.chat.id,
                       open('graphs/TEU.jpg', 'rb'))
        bot.send_message(query.message.chat.id, "You selected EU. Would you like to make another selection? "
                                                "\n\nClick on the menu to choose again!",
                         reply_markup=create_menu_keyboard())


def create_menu_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    show_menu_button = telebot.types.InlineKeyboardButton("Menu", callback_data="show_menu")
    keyboard.add(show_menu_button)
    return keyboard


bot.polling()
