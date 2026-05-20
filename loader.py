from telebot import TeleBot
from config import TOKEN
from db import Database

bot = TeleBot(token=TOKEN, parse_mode="HTML")
db = Database()
