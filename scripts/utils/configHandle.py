import yaml
from yaml import Loader
from discord.ext import commands
from scripts.utils.exceptions import Error, InvalidBotToken
import discord
class ConfigHandler:
    def __init__(self):
        print('Loading config...')
        self.intents = discord.Intents.default()
        self.intents.members = True
        with open(r'config\config.yml') as f:
            cfg = yaml.load(f, Loader=Loader)
        general = (cfg["General"])
        important = (cfg["Important"])
        visual = (cfg["Visual"])
        for key, value in important.items():
            self.ERROR = 'Please enter a valid Token in config\config.yml'
        print(general)
        print(important)
        self.TOKEN = important.get('Token')
        self.PREFIX = general.get('Prefix')
        self.ADMINS = general.get('Admins')
        self.PASSWORD = general.get('Passwd')
        self.ACTIVITY = visual.get('Activity')

    def getBotConfig(self):
        bot = commands.Bot(command_prefix=self.PREFIX, intents=self.intents)


        return bot

    def configError(self):
        print('ERROR:')
        if self.ERROR:
            print(config.ERROR)
        else:
            print('unknown error')




config = ConfigHandler()
bot = config.getBotConfig()
