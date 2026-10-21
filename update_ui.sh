#!/bin/bash
pyside6-uic ui/mainwindow.ui -o src/mainwindow_ui.py
pyside6-uic ui/settings.ui -o src/settings_ui.py
pyside6-uic ui/users.ui -o src/users_ui.py
pyside6-uic ui/newkeepass.ui -o src/newkeepass_ui.py
echo "ui файлы конвертированы"
pyside6-rcc resources/resources.qrc -o src/resources_rc.py
echo "ресурсы конвертированы"

FILE="./src/mainwindow_ui.py"
NEW_TEXT="import src.resources_rc"
sed -i "23s|.*|$NEW_TEXT|" "$FILE"
echo "$FILE обновлен"

FILE="./src/settings_ui.py"
NEW_TEXT="import src.resources_rc"
sed -i "22s|.*|$NEW_TEXT|" "$FILE"
echo "$FILE обновлен"

FILE="./src/users_ui.py"
NEW_TEXT="import src.resources_rc"
sed -i "22s|.*|$NEW_TEXT|" "$FILE"
echo "$FILE обновлен"
