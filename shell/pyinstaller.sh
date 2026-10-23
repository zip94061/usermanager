#!/bin/bash
source .venv/bin/activate
pyinstaller --clean -y --onefile --add-data ".venv/lib/python3.14/site-packages/pykeepass/blank_database.kdbx:pykeepass" usermaster.py

