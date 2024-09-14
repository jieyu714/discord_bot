import discord
from discord.ext import commands
import json
import os

# read file
with open("discord_bot/core/setting.json", 'r', encoding = "utf8") as jFile:
    jData = json.load(jFile)

# bot basic
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix = "$", intents = intents)

# bot online
@bot.event
async def on_ready():
    for Filename in os.listdir("discord_bot/function"):
        if Filename.endswith(".py"):
            await bot.load_extension(f"function.{Filename[:-3]}")
            print(f" >> {Filename} loaded successfully << ")
    print(" >> bot is online << ")

# load
@bot.command()
async def load(ctx, extension):
    try:
        await bot.load_extension(f"function.{extension}")
        await ctx.send(f"Loaded {extension} done.")
    except:
        await ctx.send(f"Unable to loaded {extension}")

# un - load
@bot.command()
async def unload(ctx, extension):
    try:
        await bot.unload_extension(f"function.{extension}")
        await ctx.send(f"Un - Loaded {extension} done.")
    except:
        await ctx.send(f"not loaded {extension}")

# reload
@bot.command()
async def reload(ctx, extension):
    try:
        await bot.reload_extension(f"function.{extension}")
        await ctx.send(f"Reloaded {extension} done.")
    except:
        await ctx.send(f"not loaded {extension}")

# bot run
if __name__ == "__main__":
  bot.run(jData["bot_token"])
