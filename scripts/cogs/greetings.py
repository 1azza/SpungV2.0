from discord.ext import commands
import discord
from scripts.utils.configHandle import config, bot
from discord.commands import slash_command, user_command
from discord.commands import Option
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @slash_command(guild_ids=config.GUILDS, description="Says Hello")
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.respond('Hello {0.name}~'.format(member))
        else:
            await ctx.respond('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

def setup(bot):
    bot.add_cog(Greetings(bot))
