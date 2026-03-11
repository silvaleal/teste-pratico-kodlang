import sqlite3

class Database:
    def __init__(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
    
    def connect(self):
        return sqlite3.connect("database.db")
        
    def query(self, query, params:tuple=()):
        self.cursor.execute(query, params)
        return self
    
    def commit(self):
        self.conn.commit()
    
    def fetchAll(self):
        result = self.cursor.fetchall()
        return result
    
    def fetchOne(self):
        result = self.cursor.fetchone()
        return result