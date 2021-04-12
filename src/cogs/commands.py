import discord
from discord.ext import commands
import sqlite3

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def create_game(self, ctx):
        pass

    @commands.command()
    async def join_game(self, ctx):
        pass

    @commands.command()
    async def kill(self, ctx, target: discord.Member):
        pass

    @commands.command()
    async def heal(self, ctx, target: discord.Member):
        pass
    
    @commands.command()
    async def ask(self, ctx, target: discord.Member):
        pass

def setup(bot):
    bot.add_cog(Commands(bot))