from discord.ext import commands
import discord
from scripts.utils.configHandle import config, bot

class Start_Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.is_owner()
    async def terminate(self, ctx):
            await ctx.reply('Bye!')
            quit()

    @commands.Cog.listener()
    async def on_ready(self):                                                                                                                   
            print(f'{bot.user} has been successfully connected to Discord!')
            activity = discord.Game(config.ACTIVITY)
            await bot.change_presence(status=discord.Status.idle, activity=activity)

def setup(bot):
    bot.add_cog(Start_Stop(bot))
