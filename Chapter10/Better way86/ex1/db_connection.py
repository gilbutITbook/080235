# db_connection.py
import __main__

class TestingDatabase:
    def __repr__(self):
        return "TestingDatabase"

class RealDatabase:
    def __repr__(self):
        return "RealDatabase"

if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = RealDatabase
