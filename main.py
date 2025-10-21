# main.py
import os,discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DEV_GUILD_ID = os.getenv("DEV_GUILD_ID")  # optional for instant slash sync
DEV_GUILD = discord.Object(id=int(DEV_GUILD_ID)) if DEV_GUILD_ID else None

intents = discord.Intents.default()
intents.message_content = True  # needed if you read message.content
bot = commands.Bot(command_prefix="!", intents=intents)

client = discord.Client(intents=intents)

@bot.event
async def setup_hook():
    # Load feature files (extensions)
    await bot.load_extension("bot.cogs.queue")
    await bot.load_extension("bot.cogs.stats")

    # Fast dev sync to one guild (appears instantly)
    if DEV_GUILD:
        bot.tree.copy_global_to(guild=DEV_GUILD)
        await bot.tree.sync(guild=DEV_GUILD)
    else:
        await bot.tree.sync()  # global (can take a while first time)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(TOKEN)
