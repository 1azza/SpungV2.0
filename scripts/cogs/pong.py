from discord.ext import commands
import discord
from scripts.utils.configHandle import config, bot
class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ping(self, ctx):
            await ctx.reply('Pong!')
    @commands.command()
    async def pp(self, ctx):
            await ctx.send('small')
def setup(bot):
    bot.add_cog(games(bot))
