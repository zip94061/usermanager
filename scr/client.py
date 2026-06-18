import random
import string
import logging

from pathlib import Path

from PySide6.QtWidgets import (
        QApplication,
        QMainWindow,
        QFileDialog,
        QInputDialog,
        QLineEdit,
        QDialog,
        QPushButton
        )
from PySide6.QtCore import Qt, QStringListModel, QObject
from PySide6.QtGui import QGuiApplication, QIcon, QAction

from scr.mainwindow_ui import Ui_MainWindow
from scr.settings_ui import Ui_Settings
from scr.users_ui import Ui_Users
from scr.cheatsheet import CheatSheet
from scr.keepass import KeePass
from scr.config import Config
from scr.logging_config import init_app_logging
from scr.sqllite import SQLite


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # logger
        init_app_logging()
        self.logger = logging.getLogger(__name__)
        self.logger.info('=' * 40)
        self.logger.info('Инициализация программы')

        # data init
        self.data = {'domain': 'stonehedge',
                     'database': None,
                     'emails_list': [],
                     'domains_list': []}
        self.sqlite = SQLite()

        # UI
        self.setupUi(self)
        self.logger.info(QGuiApplication.styleHints().colorScheme())

        # config
        self.config = Config()
        path = self.config.database_path
        self.data['database'] = path
        emails = self.config.emails
        self.data['emails_list'] = emails
        domains = self.config.domains
        self.data['domains_list'] = domains
        self.update_comboboxes()

        # line edits
        self.lineEdit_1.textChanged.connect(self.update_fields)
        self.lineEdit_1.textChanged.connect(
                lambda: self.update_data('full_name', self.lineEdit_1.text())
                )
        self.lineEdit_4.textChanged.connect(self.save_number)
        self.lineEdit_4.textChanged.connect(
                lambda: self.update_data('phone', self.lineEdit_4.text())
                )
        self.lineEdit_6.textChanged.connect(
                lambda: self.update_data('email', self.lineEdit_6.text())
                )
        self.lineEdit_8.textChanged.connect(
                lambda: self.update_data('password', self.lineEdit_8.text())
                                            )
        self.lineEdit_9.textChanged.connect(
                lambda: self.update_data('login', self.lineEdit_9.text())
                )

        # buttons
        self.pushButton.clicked.connect(self.generate_password)

        # actions
        self.action.triggered.connect(self.clear_all)
        self.action_2.triggered.connect(self.print)
        self.action_3.triggered.connect(self.save)
        self.action_4.triggered.connect(self.open_settings)
        self.action_5.triggered.connect(self.open_users)

        # settings window
        self.settings = Settings(parent=self)
        self.model = QStringListModel()
        self.model.setStringList(self.data['emails_list'])
        self.settings.ui.listView.setModel(self.model)
        self.model_2 = QStringListModel()
        self.model_2.setStringList(self.data['domains_list'])
        self.settings.ui.listView_2.setModel(self.model_2)

        # users window
        self.users = Users(parent=self)
        self.model_3 = QStringListModel()
        self.model_3.setStringList(self.sqlite.get_fullname())
        self.users.ui.listView.setModel(self.model_3)

        # combo boxes
        self.comboBox.currentIndexChanged.connect(self.update_email)
        self.comboBox_2.currentIndexChanged.connect(self.set_domain)

        self.generate_password()
        self.set_theme_icons()
        QGuiApplication.styleHints().colorSchemeChanged.connect(
                self.set_theme_icons
                )

    def closeEvent(self, event, /):
        temp = Path('temp')
        data = [i for i in temp.iterdir()]
        for i in data:
            i.unlink()
        self.logger.info('Папка temp очищена')

    def update_fields(self):
        full_name = self.lineEdit_1.text().strip()
        if ' ' in full_name:
            last_name, first_name = full_name.split(' ', 1)
        else:
            last_name = full_name
            first_name = ' '
        self.update_data('full_name', full_name)

        self.lineEdit_2.setText(last_name)
        self.lineEdit_3.setText(first_name)
        self.lineEdit_6.setText(self.transliterate(last_name.lower()))

        login = "{0}{1}".format(
                self.transliterate(first_name[0].lower()),
                self.transliterate(last_name.lower())
                )
        self.lineEdit_9.setText(login)
        self.update_data('login', login)
        self.update_email()

    def update_email(self):
        self.lineEdit_6.clear()
        maildomain = self.comboBox.currentText()
        email = "{0}{1}".format(
                self.transliterate(self.lineEdit_2.text().lower()),
                maildomain
                )
        self.lineEdit_6.setText(email)
        self.update_data('email', email)

    def set_domain(self):
        domain = self.comboBox_2.currentText()
        self.data['domain'] = domain

    def save_number(self):
        phone = self.lineEdit_4.text()
        self.update_data('phone', phone)

    def generate_password(self):
        uppercase_letters = list(string.ascii_uppercase)
        lowercase_letters = list(string.ascii_lowercase)
        digits = list(string.digits)

        password = [random.choice(uppercase_letters)]

        for _ in range(3):
            next_letter = random.choice(lowercase_letters)
            while next_letter in password:
                next_letter = random.choice(lowercase_letters)
            password.append(next_letter)
            lowercase_letters.remove(next_letter)

        for _ in range(4):
            next_digit = random.choice(digits)
            while next_digit in password:
                next_digit = random.choice(digits)
            password.append(next_digit)
            digits.remove(next_digit)

        random.shuffle(password[1:])

        password = ''.join(password)

        self.lineEdit_8.setText(password)
        self.update_data('password', password)

    def clear_all(self):
        for lineEdit in [
                self.lineEdit_1, self.lineEdit_2, self.lineEdit_3,
                self.lineEdit_4, self.lineEdit_5, self.lineEdit_6,
                self.lineEdit_7, self.lineEdit_8, self.lineEdit_9
                ]:
            lineEdit.clear()
        self.textEdit_2.clear()
        self.generate_password()

    def update_textEdit_2(self):
        self.textEdit_2.setPlainText(f'''
Созданы:
уз '{self.lineEdit_9.text()}'
п/я '{self.lineEdit_6.text()}'
тел. '{self.lineEdit_4.text()}'
''')

    def setup_copy_buttons(self):
        self.copy_text(self.lineEdit_1, self.pushButton_1)
        self.copy_text(self.lineEdit_2, self.pushButton_2)
        self.copy_text(self.lineEdit_3, self.pushButton_3)
        self.copy_text(self.lineEdit_4, self.pushButton_4)
        self.copy_text(self.lineEdit_5, self.pushButton_5)
        self.copy_text(self.lineEdit_6, self.pushButton_6)
        self.copy_text(self.lineEdit_7, self.pushButton_7)
        self.copy_text(self.lineEdit_8, self.pushButton_8)
        self.copy_text(self.lineEdit_9, self.pushButton_9)
        self.pushButton_12.clicked.connect(
                lambda: QApplication.clipboard().setText(
                    self.textEdit_2.toPlainText()
                    )
                )

    def print(self):
        if self.check_data(['full_name', 'phone', 'email']):
            cheat_sheet = CheatSheet(
                full_name=self.data['full_name'],
                login=self.data['login'],
                email=self.data['email'],
                password=self.data['password'],
                phone=self.data['phone']
            )
            cheat_sheet.make_cheat_sheet()
            message = cheat_sheet.get_message()
            if message:
                self.statusBar.setStyleSheet(
                        "QStatusBar { color: rgba(255, 0, 0, 255); }"
                        )
                self.statusBar.showMessage(message)

    def save(self):
        if self.check_data(['login', 'password', 'phone']):
            # Download database
            self.logger.info('Поиск файла базы данных')
            database = self.data['database']
            if not database or not Path(database).exists():
                self.logger.info(
                        'Файл не найден. Инициализация подключения файла'
                        )
                database = self.get_database_file()
            self.logger.info('Файл найден')
            self.update_data('database', database)
            self.config.database_path = database

            # Enter password database
            self.logger.info('Инициализация ввода пароля')
            password = self.get_database_password()
            if password:
                domain = self.data['domain']
                keepass = KeePass(database=database, password=password)

                if not keepass.get_status():
                    message = keepass.get_message()
                    self.logger.error(message)
                    self.statusBar.setStyleSheet(
                            "QStatusBar { color: rgba(255, 0, 0, 255); }"
                                                 )
                    self.statusBar.showMessage(message)
                else:
                    # save database credentials
                    self.logger.info('password введет верно')
                    self.update_data('database_password', password)

                    # check user exist
                    if keepass.get_user(self.data['login']):
                        self.statusBar.setStyleSheet(
                                "QStatusBar { color: rgba(255, 0, 0, 255); }"
                                )
                        self.statusBar.showMessage(
                               "Пользователь {0} уже существует".format(
                                   self.data['login']
                                   ),
                               timeout=1000
                                )
                    else:
                        self.sqlite.set_data(
                                self.data['full_name'],
                                self.data['login'],
                                self.data['email'],
                                self.data['phone']
                                )
                        keepass.set_user(
                                domain,
                                self.data['login'],
                                self.data['database_password']
                                )
                        self.statusBar.setStyleSheet(
                                "QStatusBar { color: rgba(0, 255, 0, 255); }"
                                )
                        self.statusBar.showMessage(
                                '{0}. {1} добавлен'.format(
                                    keepass.get_message(),
                                    self.data['login']
                                    ),
                                timeout=1000
                                )

    def check_data(self, keys: list):
        result = True
        for key in keys:
            if self.data.get(key) is None:
                message = f'Не заполенно {key}'
                self.statusBar.setStyleSheet(
                        "QStatusBar { color: rgba(255, 0, 0, 255); }"
                        )
                self.statusBar.showMessage(message, timeout=1000)
                self.logger.info(message)
                result = False
        return result

    def update_data(self, key, value):
        self.data[key] = value

    def get_database_password(self):
        password = self.data.get('database_password')
        if password is None:
            password, ok = QInputDialog.getText(
                    self,
                    'password от базы',
                    'Введите пароль:',
                    QLineEdit.EchoMode.Password,
                    ''
                    )
            if ok and password:
                return password
            else:
                message = 'Неверный пароль'
                self.statusBar.setStyleSheet(
                        "QStatusBar { color: rgba(255, 0, 0, 255); }"
                        )
                self.statusBar.showMessage(message, timeout=1000)
                self.logger.info(message)
        else:
            return password

    def get_database_file(self):
        # open database file
        database, ok = QFileDialog.getOpenFileName(
                self,
                'Открыть файл базы',
                '.',
                'KeePass Database (*.kdbx)'
                )
        if ok and database:
            return database
        else:
            message = 'Некоректный файл базы данных'
            self.statusBar.setStyleSheet(
                    "QStatusBar { color: rgba(255, 0, 0, 255); }"
                    )
            self.statusBar.showMessage(message, timeout=1000)
            self.logger.info(message)
            return None

    # Окно настроек
    def open_settings(self):
        database_path = self.data['database']

        # Настройка пути до файла базы данных
        if database_path:
            self.settings.ui.lineEdit.setText(self.data.get('database'))

        self.settings.ui.pushButton.clicked.connect(
            lambda: (
                path := self.get_database_file(),
                self.settings.ui.lineEdit.setText(path) if path else None,
                self.data.__setitem__('database', path) if path else None,
                self.data.pop('database_password', None)
            )
        )
        self.settings.ui.lineEdit.textChanged.connect(
            lambda: (
                self.update_data('database', self.settings.ui.lineEdit.text())
            )
        )

        # Настройка списка email
        self.settings.ui.pushButton_2.clicked.connect(
            lambda: (
                text := self.settings.ui.lineEdit_2.text(),
                self.settings_data_add(
                    'emails_list',
                    text,
                    self.model,
                    self.settings.ui.lineEdit_2
                    )
                if text else None
            )
        )
        self.settings.ui.pushButton_3.clicked.connect(
            lambda: self.settings_data_del(
                'emails_list',
                self.model,
                self.settings.ui.listView
                               )
        )
        # Настройка списка доменов
        self.settings.ui.pushButton_4.clicked.connect(
            lambda: (
                text := self.settings.ui.lineEdit_3.text(),
                self.settings_data_add(
                    'domains_list',
                    text, self.model_2,
                    self.settings.ui.lineEdit_3)
                if text else None
            )
        )
        self.settings.ui.pushButton_5.clicked.connect(
            lambda: self.settings_data_del(
                'domains_list', self.model_2, self.settings.ui.listView_2
                                           )
        )

        # Действие при нажатии кноки Ok
        self.settings.ui.buttonBox.accepted.connect(self.settings.accept)

        if self.settings.exec() == QDialog.DialogCode.Accepted:
            self.config.database_path = self.data['database']
            self.update_comboboxes()
            self.settings_clear_lineEdits()
        # Ниже этой строки не привязывать кнопки, они не будут работать.

    def open_users(self):
        self.users.exec()
        self.users.ui.buttonBox.accepted.connect(self.users.accept)

    def settings_data_add(
            self, data_key, value, model: QStringListModel, lineedit: QLineEdit
            ):
        self.data[data_key].append(value)
        model.setStringList(self.data[data_key])
        lineedit.clear()

    def settings_data_del(self, data_key, model, listview):
        indexes = listview.selectedIndexes()
        if not indexes:
            return
        if len(indexes) > 1:
            emails = sorted([index.row() for index in indexes], reverse=True)
            for email in emails:
                del self.data[data_key][email]
        else:
            email = indexes[0].row()
            del self.data[data_key][email]

        model.setStringList(self.data[data_key])
        listview.clearSelection()

    def settings_clear_lineEdits(self):
        self.settings.ui.lineEdit_2.clear()
        self.settings.ui.lineEdit_3.clear()

    def update_combobox(self, data_key, combobox):
        combobox.clear()
        combobox.addItems(self.data[data_key])

    def update_comboboxes(self):
        self.update_combobox('emails_list', self.comboBox)
        self.update_combobox('domains_list', self.comboBox_2)

    @staticmethod
    def transliterate(text):
        trans_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
            'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
            'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
            'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
            'э': 'e', 'ю': 'iu', 'я': 'ya',
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
            'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
            'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
            'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
            'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
            'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
            'Э': 'E', 'Ю': 'Iu', 'Я': 'Ya'
        }
        result = ''
        for char in text:
            if char in trans_dict:
                result += trans_dict[char]
            else:
                result += char
        return result

    def show_users(self):
        pass

    @staticmethod
    def copy_text(lineEdit, button):
        button.clicked.connect(
                lambda: QApplication.clipboard().setText(lineEdit.text())
                )

    def set_theme_icons(self):
        scheme = QGuiApplication.styleHints().colorScheme()
        if scheme == Qt.ColorScheme.Light:
            target_theme = "light_theme"
        else:
            target_theme = "dark_theme"
        for button in self.findChildren(QObject):
            if isinstance(button, (QPushButton, QAction)):
                icon_name = button.property('iconName')
                if icon_name:
                    new_icon_path = ':/{0}/icons/{1}/{2}.svg'.format(
                            target_theme, target_theme, icon_name
                            )
                    button.setIcon(QIcon(new_icon_path))


class Settings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)


class Users(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Users()
        self.ui.setupUi(self)
