import sqlite3
from datetime import datetime


class Database:
    def __init__(self):
        self.con = sqlite3.connect("anonbot.db", check_same_thread=False)
        self.cur = self.con.cursor()

    # ================= USERS =================

    def create_users_table(self):
        SQL = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL UNIQUE,
            username TEXT,
            full_name TEXT,
            date_joined DATETIME
        )
        """
        self.cur.execute(SQL)
        self.con.commit()

    def is_exists_user(self, user_id) -> bool:
        SQL = "SELECT id FROM users WHERE user_id=?"
        self.cur.execute(SQL, (user_id,))
        return bool(self.cur.fetchone())

    def register_user(self, user_id, username=None, fullname=None):
        if self.is_exists_user(user_id):
            print("User mavjud")
            return

        now = datetime.now().strftime("%d-%m-%Y %H:%M")

        SQL = """
        INSERT INTO users(user_id, username, full_name, date_joined)
        VALUES (?, ?, ?, ?)
        """

        self.cur.execute(SQL, (user_id, username, fullname, now))
        self.con.commit()

        print("Yangi user yaratildi:", user_id)

    # ================= QUEUE =================

    def create_queue_table(self):
        SQL = """
        CREATE TABLE IF NOT EXISTS queue(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE
        )
        """

        self.cur.execute(SQL)
        self.con.commit()

    def insert_into_queue(self, user_id):

        is_have = self.get_user_active_room(user_id)
        if not is_have:
            SQL = "SELECT id FROM queue WHERE user_id=?"
            self.cur.execute(SQL, (user_id,))

            if self.cur.fetchone():
                return

        SQL = "INSERT INTO queue(user_id) VALUES (?)"
        self.cur.execute(SQL, (user_id,))
        self.con.commit()

    def remove_from_queue(self, user_id):
        SQL = "DELETE FROM queue WHERE user_id=?"
        self.cur.execute(SQL, (user_id,))
        self.con.commit()

    def get_random_user_from_queue(self, user_id):
        SQL = """
        SELECT user_id
        FROM queue
        WHERE user_id != ?
        ORDER BY RANDOM()
        LIMIT 1
        """

        self.cur.execute(SQL, (user_id,))
        return self.cur.fetchone()

    # ================= ROOM =================

    def create_room_table(self):
        SQL = """
        CREATE TABLE IF NOT EXISTS room(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user1 INTEGER,
            user2 INTEGER,
            status TEXT DEFAULT 'active'
        )
        """

        self.cur.execute(SQL)
        self.con.commit()

    def add_users_to_room(self, user1, user2):
        self.remove_from_queue(user1)
        self.remove_from_queue(user2)

        SQL = """
        INSERT INTO room(user1, user2)
        VALUES (?, ?)
        """

        self.cur.execute(SQL, (user1, user2))
        self.con.commit()

        print("Yangi xona yaratildi!")

    def get_user_active_room(self, user_id):
        SQL = """
        SELECT id, user1, user2
        FROM room
        WHERE (user1=? OR user2=?)
        AND status='active'
        """

        self.cur.execute(SQL, (user_id, user_id))
        return self.cur.fetchone()

    def close_room(self, user_id):
        SQL = """
        UPDATE room
        SET status='inactive'
        WHERE (user1=? OR user2=?)
        AND status='active'
        """

        self.cur.execute(SQL, (user_id, user_id))
        self.con.commit()