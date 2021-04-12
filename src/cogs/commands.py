import discord
from discord.ext import commands
import sqlite3
import re

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def create_game(self, ctx):
        main = sqlite3.connect('main.sqlite')
        cur = main.cursor()
        cur.execute(f"SELECT guild_id FROM main WHERE guild_id = '{ctx.guild.id}'")
        result = cur.fetchone()
        if result is None:
            def check(message):
                return message.author.id == ctx.message.author.id and message.channel == ctx.channel

            await ctx.send('Please answer this questions in 15 seconds for each one. Do not use negative or decimal numbers or letters.')
            questions = ['How many werewolfs do you want?', 'How many doctors do you want?', 'How many detectives do you want?']
            answers = []
            for question in questions:
                await ctx.send(question)
                answer = await self.bot.wait_for('message', check=check, timeout=15.0)
                try:
                    is_good_answer = int(answer.content)
                    other_check = bool(re.match(r'^-?\d+(\.\d+)?$', answer.content))
                    if other_check:
                        answers.append(answer.content)
                    else:
                        await ctx.send('I said do not use negative or decimal numbers')
                except Exception as e:
                    print(e)
                    await ctx.send('I said do not use letters!')

            sql = (f"INSERT INTO main(guild_id,werewolf_count,doctors_count,detectives_count) VALUES(?,?,?,?)")
            val = (ctx.guild.id, answers[0], answers[1], answers[2])
            print('Created game')
            cur.execute(sql, val)
            main.commit()              
        else:
            await ctx.send('You already started a game.')
        cur.close()
        main.close()

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