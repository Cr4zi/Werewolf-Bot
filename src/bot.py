import discord
from discord.ext import commands
import os
import sqlite3
from dotenv import load_dotenv
load_dotenv()

class Werewolf(commands.Bot):
    def __init__(self):
        intents = discord.Intents(
            guilds=True,
            members=True,
            bans=True,
            emojis=True,
            voice_states=True,
            messages=True,
            reactions=True,
        )
        super().__init__(command_prefix='>', intents=intents)

        main = sqlite3.connect('main.sqlite')
        cursor = main.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
            usr_id TEXT,
            money TEXT,
            start_time TEXT,
            end_time TEXT
        ''')


        self.load_extension('cogs.commands')

    async def on_ready(self):
        print('Connected as:', self.user)

werewolf = Werewolf()
werewolf.run(os.getenv("BOT_TOKEN"))