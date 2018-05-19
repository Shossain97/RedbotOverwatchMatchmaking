import os
import discord
from __main__ import send_cmd_help
from cogs.utils import checks
from discord.ext import commands
from discord.ext.commands import formatter

from .utils.dataIO import dataIO
import tkinter as tk

##a general user
class User:
    def __init__(self, userName, userCode, userBlizzardID, userRole):
        self.userName = userName
        self.userCode = userCode
        self.userBlizzardID = userBlizzardID
        self.userRole = userRole


##the admin's initial command
class OverwatchMatchQueue:
    def __init__(self, bot):
        self.bot = bot
        self.banlist = dataIO.load_json("data/OverwatchMatchQueue/banlist.json")
    
    @commands.command()
    async def overwatchQueueStart(self):
    ###generate GUI interface###
    ##await selections
        root = tk.Tk()

        w = tk.Label(root, text="Hello Tkinter!")
        w.pack()

        root.mainloop()

def checkFolders():
    folder = "data/OverwatchMatchQueue"
    if not os.path.exists(folder):
        print("Creating {} folder...".format(folder))
        os.makedirs(folder)

def checkFiles():
    banlist = {'battletags': {}}
    if not dataIO.is_valid_json("data/OverwatchMatchQueue/banlist.json"):
        print("Creating banlist ...")
        dataIO.save_json("data/OverwatchMatchQueue/banlist.json", banlist)

def setup(bot):
    checkFolders()
    checkFiles()
    bot.add_cog(OverwatchMatchQueue(bot))
    