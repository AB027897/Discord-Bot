import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='!')


client = discord.Client()


@bot.event
async def on_ready():
    print(f' {client.user} has connected!')


@client.event
async def on_message(message):
    if message.content == "1":
        response = "Hello"
        await message.channel.send(response)
bot.run(TOKEN)
