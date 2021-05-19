import os
import discord
from dotenv import load_dotenv

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    await client.Guild.text_channels[-1].send(f'{client.user.name} has connected to Discord!')
    #print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


client.run(TOKEN)

#