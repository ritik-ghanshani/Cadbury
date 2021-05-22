import os
import sys
import discord
import time
from pprint import pprint
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from pymongo import MongoClient

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
password = os.environ['MONGODB_PASSWD']


client = MongoClient(f'mongodb+srv://ritik:{password}@cadburycluster.oxq3b.mongodb.net/CadburyDB.Cadbury?retryWrites=true&w=majority')
db = client['CadburyDB']['Cadbury']


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

@bot.command(name="hello", help="just echoes back what you said")
async def message(ctx):
    print(f'{ctx.message.author.name} said {" ".join(ctx.message.content.split(" ")[1:])}', flush=True)
    await ctx.channel.send(" ".join(ctx.message.content.split(" ")[1:]), tts=False)

@slash.slash(name="hello", description="just echoes back what you said", options= [
    create_option(
      name= "content",
      description= "type your message here",
      option_type= 3,
      required=True
    )
  ])
async def _hello(ctx: SlashContext, content: str):
    print(f'{ctx.author.name} said {ctx.args[0]}', flush=True)
    await ctx.send(ctx.args[0], tts=False)

bot.run(TOKEN)