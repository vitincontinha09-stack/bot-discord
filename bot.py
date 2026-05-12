import os
import discord
from discord.ext import commands

TOKEN = os.getenv("MTUwMzQ3NzQ1Nzg2MzQ0NjU5OA.G32Jde.5X09kovrV9nFx72u4X2uMqP2cOa6rFGcJoYLJk")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=".",
    intents=intents
)
bot.run(TOKEN)
