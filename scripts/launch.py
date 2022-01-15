from scripts.utils.configHandle import config, bot
from discord.ext.commands import Bot
import discord
from scripts.utils.exceptions import *
import asyncio
import os


def launch():
    print(config.BLUE + 'Cogs loading...')
    for file_name in os.listdir('scripts/cogs'):
        if file_name.endswith('.py'):
            bot.load_extension(f'scripts.cogs.{file_name[:-3]}')
            print('cog found:', config.GREEN + file_name)
    



    print(config.BLUE + 'Establishing connection to discord api...')
    print('-\n-\n-\n-')


    try:
        bot.run(config.TOKEN)
    except:
        config.configError()
