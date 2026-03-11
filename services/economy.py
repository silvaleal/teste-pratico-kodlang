from database import Database
from datetime import datetime


class EconomyServices:
    def __init__(self):
        self.database = Database()
       
    def transfer(self, user, target, amount):
        if amount <= 0:
            raise Exception("Quantia inválida.")

        userInfos = self.get(user.id)
        
        if float(userInfos[2]) < amount:
            raise Exception("Saldo insuficiente.")
        
        try:
            self.database.query("UPDATE users SET coins = coins - ? WHERE userId = ?", (amount, user.id))
            self.database.query("UPDATE users SET coins = coins + ? WHERE userId = ?", (amount, target.id))
            self.database.commit()  
            return True
        except Exception as e:
            raise Exception(e)
        
    def saveRank(self, data):
        return self.database.query("INSERT INTO baltop_history (savedAt, infos) VALUES (?, ?)", (datetime.now(), f"{data}", )).commit()
    
    def get(self, targetId):
        infos = self._getInfos(targetId)
        
        if not infos:
            self.database.query("INSERT INTO users (userId) VALUES (?)", (targetId, )).commit()
            infos = self._getInfos(targetId)
            
        return infos
    
    def getRank(self):
        return self.database.query("SELECT * FROM users ORDER BY coins DESC LIMIT 10;").fetchAll()
    
    def getLastRank(self):
        return self.database.query("SELECT * FROM baltop_history ORDER BY savedAt DESC LIMIT 1;").fetchOne()
    
    def _getInfos(self, targetId):
        return self.database.query('SELECT * FROM users WHERE userId = ?', (targetId, )).fetchOne()
