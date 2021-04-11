import discord
from discord.ext import commands
import os
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

        self.load_extension('cogs.commands')

    async def on_ready(self):
        print('Connected as:', self.user)

werewolf = Werewolf()
werewolf.run(os.getenv("BOT_TOKEN"))