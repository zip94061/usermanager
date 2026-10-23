cd ..\
.\.venv\Scripts\pyinstaller --clean -y --onefile --windowed --add-data ".venv\lib\site-packages\pykeepass\blank_database.kdbx:pykeepass" usermaster.py
