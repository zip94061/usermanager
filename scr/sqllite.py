import sqlite3
from pathlib import Path

import logging


class SQLite:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.database = Path("data", "usersdata.db")
        self.database.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
                           """
                           SELECT name
                           FROM sqlite_master
                           WHERE type='table'
                            AND name='users'
                           """
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

    def find_user(self, login):
        self.cursor.execute(
                        "SELECT login FROM users WHERE login = ?", (login,)
                        )
        return self.cursor.fetchone()

    def set_data(self, full_name, login, email, phone):
        user = self.find_user(login)
        if not user:
            self.logger.info('Новый пользователь')
            data = [(full_name, login, email, phone)]
            self.cursor.executemany(
                    "INSERT INTO users VALUES(?, ?, ?, ?)",
                    data
                    )
        else:
            data = [(full_name, email, phone, login)]
            self.cursor.executemany(
                    """UPDATE users
                    SET full_name = ?, email = ?, phone = ? WHERE login = ?""",
                    data)
            self.logger.info('Пользователь обновлен')
        self.connection.commit()

    def get_fullname(self):
        self.cursor.execute("SELECT full_name, login FROM users")
        return [f"{user[0]}, {user[1]}" for user in self.cursor.fetchall()]

    def get_user_data(self, login):
        self.cursor.execute(
                "SELECT * FROM users WHERE login = ?", (login,)
                )
        return self.cursor.fetchall()

    def del_user_data(self, login):
        print('sqlite', login)
        user = self.find_user(login)
        if user:
            self.cursor.execute(
                    "DELETE FROM users WHERE login = ?", (login,)
                    )
            self.connection.commit()
            self.logger.info(f'{login} удален')
        else:
            self.logger.info(f'{login} не найден')
