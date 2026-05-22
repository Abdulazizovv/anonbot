from telebot import types
from loader import bot, db


@bot.message_handler(func=lambda message: True)
def all_message_handler(message: types.Message):

    room = db.get_user_active_room(message.from_user.id)

    if not room:
        bot.send_message(
            message.from_user.id,
            "❌ Noma'lum buyruq"
        )
        return

    room_id, user1, user2 = room

    # suhbatdoshni aniqlash
    if message.from_user.id == user1:
        suhbatdosh_id = user2
    else:
        suhbatdosh_id = user1

    try:
        bot.copy_message(
            chat_id=suhbatdosh_id,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

    except Exception as err:
        print("Message forward error:", err)

        bot.send_message(
            message.from_user.id,
            "❌ Xabar yuborilmadi"
        )