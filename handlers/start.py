from telebot import types
from loader import bot, db
from keyboards import main_menu


@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    try:
        db.register_user(
            user_id=message.from_user.id,
            username=message.from_user.username,
            fullname=message.from_user.full_name,
        )
    except:
        pass
    bot.send_message(
        message.from_user.id, "Assalomu alaykum anonim suhbat botga xush kelibsiz!",
        reply_markup=main_menu
    )
