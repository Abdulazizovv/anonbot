from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton



main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton("Suhbatdosh qidirish🔎")
main_menu.add(btn1)