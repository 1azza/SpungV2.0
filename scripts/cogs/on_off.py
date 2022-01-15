from discord.ext import commands
import discord
from scripts.utils.configHandle import config, bot
from discord.commands import slash_command, user_command
from discord.commands import Option
class Start_Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @slash_command(guild_ids=config.GUILDS, description="Shuts Down Bot (Only works if you own it)")
    @commands.is_owner()
    async def terminate(self, ctx):
            await ctx.respond('Bye!')
            quit()

    @commands.Cog.listener()
    async def on_ready(self):
            print(config.GREEN + f'{bot.user} has been successfully connected to Discord!')
            print('-\n-\n-\n-')
            activity = discord.Game(config.ACTIVITY)
            await bot.change_presence(status=discord.Status.idle, activity=activity)

def setup(bot):
    bot.add_cog(Start_Stop(bot))
