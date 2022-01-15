import yaml
from yaml import Loader
from discord.ext import commands
from scripts.utils.exceptions import Error, InvalidBotToken
import discord
class ConfigHandler:
    def __init__(self):
        print('Loading config...')
        self.ERROR = 0
        self.intents = discord.Intents.default()
        self.intents.members = True
        with open(r'config\config.yml') as f:
            cfg = yaml.load(f, Loader=Loader)
        general = (cfg["General"])
        important = (cfg["Important"])
        visual = (cfg["Visual"])
        self.TOKEN = important.get('Token')
        def set():
            self.PREFIX = general.get('Prefix')
            self.ADMINS = general.get('Admins')
            self.PASSWORD = general.get('Passwd')
            self.ACTIVITY = visual.get('Activity')
            self.GUILDS = general.get('Guilds')
            print(self.GUILDS)
            print('Found Token!')
            print(self.TOKEN)

        if self.TOKEN == None:
            try:
                with open(r'config\secret.txt') as f:
                        print('Looking in secret.txt')
                        self.TOKEN = f.readline()
                if len(self.TOKEN) > 10:
                    set()
                else:
                    self.ERROR = 'Please enter a valid Token in config\secret.txt'


            except:
                self.ERROR = 'Please enter a valid Token in config\config.yml'


        else:
            set()



    def getBotConfig(self):
        bot = commands.Bot(command_prefix=self.PREFIX, intents=self.intents)


        return bot

    def configError(self):
        if self.ERROR:
            print(self.ERROR)
            quit()
        pass







config = ConfigHandler()
config.configError()
bot = config.getBotConfig()
