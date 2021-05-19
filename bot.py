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
    sys.stdout.write(f'{ctx.message.author.name} said {" ".join(ctx.message.content.split(" ")[1:])}', flush=True)
    await ctx.channel.send(" ".join(ctx.message.content.split(" ")[1:]))
    await ctx.channel.send(ctx.message.attachments[0].proxy_url)

@slash.slash(name="hello")
async def _hello(ctx: SlashContext):
    await ctx.send(content="never gonna let you down, never gonna run around")

bot.run(TOKEN)