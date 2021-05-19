import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

client = discord.Client()
slash = SlashCommand(bot, sync_commands=True)

@client.event
async def on_ready():
    #await client.guilds[0].text_channels[-1].send(f'{client.user.name} has connected to Discord!')
    print(f'{bot.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name="hello")
async def message(message):
    await message.channel.send(" ".join(message.message.content.split(" ")[1:]))

@slash.slash(name="hello")
async def _hello(ctx: SlashContext):
    await ctx.send(content="never gonna let you down, never gonna run around")


bot.run(TOKEN)
#client.run(TOKEN)