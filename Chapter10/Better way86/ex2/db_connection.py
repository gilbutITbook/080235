# db_connection.py
import sys

class Win32Database:
    def __repr__(self):
        return "Win32Database"

class PosixDatabase:
    def __repr__(self):
        return "PosixDatabase"

if sys.platform.startswith('win32'):
    Database = Win32Database
else:
    Database = PosixDatabase
