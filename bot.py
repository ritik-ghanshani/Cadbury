import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

@bot.command(name="hello", help="just echoes back what you said")
async def message(ctx):
    print(f'{ctx.message.author.name} said {" ".join(ctx.message.content.split(" ")[1:])}', flush=True)
    await ctx.channel.send(" ".join(ctx.message.content.split(" ")[1:]), tts=False)

@slash.slash(name="hello", description="just echoes back what you said", options= [
    {
      "name": "Message",
      "description": "type your message here",
      "type": 3,
      "required": "true"
    }
  ])
async def _hello(ctx: SlashContext):
    print(f'{ctx.message.author.name} said {" ".join(ctx.message.content.split(" ")[1:])}', flush=True)
    await ctx.channel.send(" ".join(ctx.message.content.split(" ")[1:]), tts=False)

bot.run(TOKEN)