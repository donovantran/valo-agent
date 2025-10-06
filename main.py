# main.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # needed if you read message.content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if message.content.lower() == "hello":
        await message.channel.send("hey dirtbag")

client.run(TOKEN)
