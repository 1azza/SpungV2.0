from scripts.utils.getToken import getTokens
from scripts.utils.configHandle import config, bot
from discord.ext.commands import Bot
import discord
from scripts.utils.exceptions import *
import asyncio
import os
def launch():
    print('Cogs loading...')
    for file_name in os.listdir('scripts/cogs'):
        if file_name.endswith('.py'):
            bot.load_extension(f'scripts.cogs.{file_name[:-3]}')
            print('cog found:', file_name)

    print(bot.cogs)
    print(bot.commands)
    print('Establishing connection to discord api...')


    try:
        bot.run(config.TOKEN)
    except:
        config.configError()
