from telebot import types
from loader import bot, db
from keyboards import main_menu


@bot.message_handler(func=lambda message: message.text == "Suhbatdosh qidirish🔎")
def search_handler(message: types.Message):
    user_id = message.from_user.id

    try:
        # foydalanuvchini navbatga qo'shamiz
        db.insert_into_queue(user_id)

        bot.send_message(user_id, "🔎 Suhbatdosh qidirilmoqda...")

        # navbatdan random user olish
        suhbatdosh = db.get_random_user_from_queue(user_id)
        print(suhbatdosh)

        if not suhbatdosh:
            bot.send_message(
                user_id,
                "⏳ Hozircha suhbatdosh topilmadi. Kutib turing...",
                reply_markup=main_menu
            )
            return

        partner_id = suhbatdosh[0]

        # ikkala userni roomga qo'shish
        db.add_users_to_room(user_id, partner_id)

        # navbatdan o'chirish
        db.remove_from_queue(user_id)
        db.remove_from_queue(partner_id)

        # xabar yuborish
        bot.send_message(
            user_id,
            "✅ Suhbatdosh topildi! Suhbatni boshlang."
        )

        bot.send_message(
            partner_id,
            "✅ Sizga suhbatdosh topildi! Suhbatni boshlang."
        )

    except Exception as err:
        print("Qidirishda xatolik:", err)

        bot.send_message(
            user_id,
            "❌ Xatolik yuz berdi."
        )