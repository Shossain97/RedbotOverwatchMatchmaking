import discord
from discord.ext import commands

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
    
    @commands.command()
    async def overwatchQueueStart(self):
    ###generate GUI interface###
    ##await selections
        root = tk.Tk()

        w = tk.Label(root, text="Hello Tkinter!")
        w.pack()

        root.mainloop()


def setup(bot):
    bot.add_cog(OverwatchMatchQueue(bot))
    