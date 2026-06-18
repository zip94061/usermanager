import sqlite3
from pathlib import Path

import logging


class SQLite:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.database = Path("database", "usersdata.db")
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
                           "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
                            )
        if not self.cursor.fetchone():
            self.logger.info('Создаю таблицу')
            print('Создаю таблицу')
            self.cursor.execute("""
                                CREATE TABLE users (
                                    full_name TEXT,
                                    login TEXT,
                                    email TEXT,
                                    phone TEXT
                                    )
                                """)
            self.connection.commit()

    def set_data(self, full_name, login, email, phone):
        self.cursor.execute(
                "SELECT login FROM users WHERE login = ?", (login,)
                )
        if not self.cursor.fetchone():
            self.logger.info('Новый пользователь')
            data = [(full_name, login, email, phone)]
            self.cursor.executemany("INSERT INTO users VALUES(?, ?, ?, ?)", data)
        else:
            data = [(full_name, email, phone, login)]
            self.cursor.executemany("UPDATE users SET full_name = ?, email = ?, phone = ? WHERE login = ?", data)
            self.logger.info('Пользователь обновлен')
        self.connection.commit()

    def get_fullname(self):
        self.cursor.execute("SELECT full_name FROM users")
        return [user[0] for user in self.cursor.fetchall()]

    def get_user_data(self, full_name):
        self.cursor.execute("SELECT * FROM users WHERE full_name = ?", (full_name,))
        return self.cursor.fetchall()
