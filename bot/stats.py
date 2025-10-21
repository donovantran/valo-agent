import discord
from discord import app_commands
from discord.ext import commands

class Stats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="stats", description="Show your stats")
    async def stats(self, itx: discord.Interaction):
        await itx.response.send_message("K/D: 1.25 • Win%: 53%", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Stats(bot))