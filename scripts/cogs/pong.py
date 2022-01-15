from discord.ext import commands
import discord
from scripts.utils.configHandle import config, bot
from discord.commands import slash_command, user_command
from discord.commands import Option
import random
class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @slash_command(description="Test the bots speed")
    async def ping(self, ctx):
            await ctx.respond('Pong! {0}'.format(bot.latency))



    @slash_command(description="How big is you PP?")
    async def pp(self, ctx):
            await ctx.respond('small')

    @slash_command(guild_ids=[861316984360402974], description="Random number from 1-100")
    async def number(self, ctx):
            await ctx.respond(random.randint(1, 100))
def setup(bot):
    bot.add_cog(games(bot))
