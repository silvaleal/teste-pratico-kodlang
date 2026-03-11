import discord
from discord.ext import commands

from container.economy import PayContainer

class Pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.container = PayContainer()

    @commands.command()
    async def pay(self, ctx, target:discord.Member=None, amount:int=None):
        
        if not target or not amount:
            return await ctx.reply("Uso correto: !pay @user quantia")
        
        if ctx.author == target:
            return await ctx.reply('Você não pode doar para você mesmo.')
        
        try:
            self.container.economyService.transfer(ctx.author, target, amount)
            await ctx.reply("Transferência realizada.")
        except Exception as e:
            await ctx.reply(e)

    @commands.command()
    async def balance(self, ctx, target:discord.Member=None):
        target = target or ctx.author
        
        await ctx.reply(embed=self.container.embedProfile(ctx, target))

    @commands.command()
    async def baltop(self, ctx):
        await ctx.reply(embed=self.container.embedRank(ctx))
        
    @commands.command()
    async def last_baltop(self, ctx):
        await ctx.reply(embed=self.container.embedLastRank(ctx))

async def setup(bot):
    await bot.add_cog(Pay(bot))
