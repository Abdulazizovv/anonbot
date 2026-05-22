from loader import bot, db
from utils import send_start_notification
import handlers

if __name__ == "__main__":
    db.create_users_table()
    db.create_queue_table()
    db.create_room_table()

    send_start_notification(bot)
    bot.infinity_polling()
