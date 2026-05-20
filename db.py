import sqlite3


class Database:
    con = sqlite3.connect("anonbot.db", check_same_thread=False)
    cur = con.cursor()

    def create_users_table(self):
        SQL = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id CHAR(100) NOT NULL UNIQUE,
username CHAR(255),
full_name CHAR(512),
date_joined DATETIME
)
"""
        self.cur.execute(SQL)
        self.con.commit()

    def is_exists_user(self, user_id) -> bool:
        SQL = "SELECT id FROM users WHERE user_id = ?"
        self.cur.execute(SQL, (user_id,))
        data = self.cur.fetchone()
        return bool(data)

    def register_user(self, user_id, username=None, fullname=None):
        from datetime import datetime

        now = datetime.now().strftime("%d-%m-%Y %H:%M")

        is_exists = self.is_exists_user(user_id)

        if not is_exists:
            SQL = """
    INSERT INTO users(user_id, username, full_name, date_joined) VALUES
    (?, ?, ?, ?)
    """
            self.cur.execute(SQL, (user_id, username, fullname, now))
            self.con.commit()
            print("Yangi user yaratildi:", user_id)
            return

        print("Allaqachon mavjud")
