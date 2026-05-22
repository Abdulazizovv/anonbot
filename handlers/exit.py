from telebot import types
from loader import bot, db


@bot.message_handler(commands=["exit"])
def exit_room(message: types.Message):
    db.close_room(message.from_user.id)
    bot.send_message(message.from_user.id, "Xona yopildi!")