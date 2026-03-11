import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

from notifications import DiscordNotification
from services.economy import EconomyServices

load_dotenv()

class App(commands.Bot):
    def __init__(self):
        self.economyService = EconomyServices()
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        
    async def setup_hook(self):
        self.saveBaltop.start()
        
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")
                
    @tasks.loop(hours=24)            
    async def saveBaltop(self):

        rank = self.economyService.getRank() 
        
        resultFinal = []
        
        for posRank in rank:
            resultFinal.append({
                "id": posRank[0],
                "userId": posRank[1],
                "coins": posRank[2]
            })
        
        self.economyService.saveRank(resultFinal)
        
        DiscordNotification().post()
                
app = App()
app.run(os.getenv("BOT_TOKEN"))