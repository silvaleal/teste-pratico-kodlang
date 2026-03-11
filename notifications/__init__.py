import requests
from database import Database
from services.economy import EconomyServices
import os

# Nota: eu poderia trocar o formato e instanciar a classe Notification com depedência da DiscordNotification

class Notification:
    def post(self): # Salvar quando notificação foi enviada.
        self.send()
        
    def send(self): # será polimorfizado, não escreva nada.
        ...

class DiscordNotification(Notification):
    def __init__(self):
        self.baseURL = os.getenv("RANK_SAVED")
        super().__init__()
        
    def send(self):
        
        requi = requests.post(self.baseURL, data={
            "content": "**KODLANG**: Histórico dos mais ricos foram salvos eternamente."
        })