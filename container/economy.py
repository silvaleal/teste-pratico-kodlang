from services.economy import EconomyServices
import discord
import json
import ast

class PayContainer:
    def __init__(self):
        self.economyService = EconomyServices()
    
    def embedProfile(self, interaction, target):
        targetInfo = self.economyService.get(target.id)
        
        embed = discord.Embed(title=f"{target.name}", description=f"Saldo de {target.mention}: R${targetInfo[2]}")
        return embed
    
    def embedRank(self, interaction):
        users = self.economyService.getRank()
        
        rank = [f"{index}. <@{user[1]}> | R${float(user[2])}" for index, user in enumerate(users)]
        
        embed = discord.Embed(title=f"Usuários mais ricos", description="\n".join(rank))
        return embed
    
    def embedLastRank(self, interaction):
        
        rank = self.economyService.getLastRank()
        
        jsonFinal = ast.literal_eval(rank[2])
        
        members = [f"{index}. <@{user['userId']}> | R${float(user['coins'])}" for index, user in enumerate(jsonFinal)]
        
        embed = discord.Embed(title=f"Usuários mais ricos", description=f"\n".join(members))
        embed.set_footer(text=f"Quanto foi salvo: {rank[1]}", icon_url="")
        return embed