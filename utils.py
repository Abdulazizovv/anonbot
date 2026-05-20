from telebot import TeleBot
from config import ADMINS
from time import sleep
import logging


def send_start_notification(bot: TeleBot):
    if not ADMINS:
        return

    for admin in ADMINS:
        try:
            bot.send_message(admin, "Bot ishga tushdi")
            sleep(0.5)
        except:
            pass

    logging.info("Bot ishga tushdi")
