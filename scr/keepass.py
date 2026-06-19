import logging

from pykeepass import PyKeePass, exceptions


class KeePass:
    def __init__(self, password, database):
        self.logger = logging.getLogger(__name__)
        self.status = False
        self.message = ''
        self.database = self.set_database(database, password)

    def get_user(self, username):
        user = self.database.find_entries(title=username, first=True)
        if user is None:
            return None
        else:
            return user

    def set_user(self, groupname, username, password):
        self.logger.debug(f'Поиск пользоваля {username}')
        if self.get_group(groupname) is None:
            self.set_group(groupname)
            self.logger.info(f'Создана группа {groupname}')
            self.database.save()
            self.logger.info('База данных сохранена')
        else:
            self.logger.info(f'Найдена группа {groupname}')
        group = self.get_group(groupname)
        user = self.get_user(username)
        if user:
            user.username = username
            user.password = password
        else:
            self.logger.info('Создан новый пользователь')
            # print('Create new user')
            self.database.add_entry(group, username, username, password)
            self.logger.info(f'Добавлена запись {username}')
        self.database.save()
        self.logger.info('База данных сохранена')

    def get_group(self, groupname):
        group = self.database.find_groups(name=groupname, first=True)
        return group

    def set_group(self, groupname):
        self.database.add_group(self.database.root_group, groupname)
        self.database.save()

    def get_database(self):
        return self.database

    def set_database(self, database, password):
        result = None
        try:
            result = PyKeePass(database, password)
            self.message = 'Успешно сохранено'
            self.status = True
        except exceptions.CredentialsError:
            self.message = 'Неверный Пароль'
        except (
                exceptions.HeaderChecksumError, exceptions.PayloadChecksumError
                ):
            self.message = 'Файл базы данных поврежден'
        except FileNotFoundError:
            self.message = 'Нет такого файла базыданных'
        except Exception as error:
            print(error)
            self.message = 'Неизвестная ошибка'
        return result

    def get_status(self):
        return self.status

    def get_message(self):
        return self.message

    def get_users(self):
        users = [user for user in self.database.entries]
        return users

    def get_user_password(self, username):
        user = self.get_user(username)
        if user:
            return user.password

    def del_user(self, username):
        user = self.get_user(username)
        print(user)
        if user:
            self.database.delete_entry(user)
            self.database.save()
            self.logger.info(f'{username} удален')
        else:
            self.logger.info(f'{username} не найден')
