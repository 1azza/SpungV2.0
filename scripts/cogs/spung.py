import discord
from discord.ext import commands
from scripts.utils.configHandle import config, bot
import cv2
import numpy as np
import re

class spung_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    async def main_spung(self, ctx):
        imgCanny =  cv2.Canny(self.IMG, 100, 100)
        cv2.imwrite("profilepicture.png", imgCanny)
        await ctx.send(file=discord.File('profilepicture.png'))

    @commands.command()
    async def spung(self, ctx, arg):
            user = re.sub("[^0-9]", "", arg)
            user = await bot.fetch_user(user)
            await user.avatar_url_as(format="png").save(fp="profilepicture.png")
            self.IMG = cv2.imread('profilepicture.png')
            await self.main_spung(ctx)


    @commands.command()
    async def spungbomb(self, ctx):
        for member in ctx.guild.members:
             await member.avatar_url_as(format="png").save(fp="profilepicture.png")
             self.IMG = cv2.imread('profilepicture.png')
             await self.main_spung(ctx)

    @commands.command()
    async def spunk(self, ctx):
        def check(message):
            return message.author == ctx.author and bool(message.attachments)
        await ctx.send('**Waiting for an attachment...**')
        resp = await bot.wait_for('message', check=check)
        image = resp.attachments[0]
        await image.save(fp="profilepicture.png")
        self.IMG = cv2.imread('profilepicture.png')
        await self.main_spung(ctx)



def setup(bot):
    bot.add_cog(spung_commands(bot))
