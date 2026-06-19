#!/bin/zsh
pyside6-uic ui/mainwindow.ui -o scr/mainwindow_ui.py
pyside6-uic ui/settings.ui -o scr/settings_ui.py
pyside6-uic ui/users.ui -o scr/users_ui.py
echo "ui файлы конвертированы"
pyside6-rcc resources/resources.qrc -o scr/resources_rc.py
echo "ресурсы конвертированы"

FILE="./scr/mainwindow_ui.py"
NEW_TEXT="import scr.resources_rc"
sed -i "23s|.*|$NEW_TEXT|" "$FILE"
echo "$FILE обновлен"

FILE="./scr/settings_ui.py"
NEW_TEXT="import scr.resources_rc"
sed -i "22s|.*|$NEW_TEXT|" "$FILE"
echo "$FILE обновлен"

FILE="./scr/users_ui.py"
NEW_TEXT="import scr.resources_rc"
sed -i "21s|.*|$NEW_TEXT|" "$FILE"
echo "$FILE обновлен"
