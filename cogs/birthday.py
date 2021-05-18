import discord
import 
from discord.ext import commands

class birthday(commands.Cog):
    """Birthday related commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="birthday")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def birthday(self, ctx):
        embed = discord.Embed(title="Discord's Birthday", description="Discord's Official Birthday is on 5/13/2015")

def setup(bot):
    bot.add_cog(birthday(bot))
