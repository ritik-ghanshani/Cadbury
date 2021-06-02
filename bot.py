import os
import sys
import discord
import time
import database as db
import psycopg2
from Task import Task
from pprint import pprint
from discord.ext import commands
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']

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

@slash.slash(name="add_task", description="add a task", options= [
    create_option(
      name= "class_name",
      description= "Class for which the task belongs to in SUB NUM format. Ex: CI 101",
      option_type= 3,
      required=True
    ),
    create_option(
      name= "description",
      description= "Description of the task (Max. 255 characters)",
      option_type= 3,
      required=True
    ),
    create_option(
      name= "due_date",
      description= "Due date of the task (MM-DD-YYYY or today/tomorrow/yesterday).",
      option_type= 3,
      required=True
    ),
    create_option(
      name= "due_time",
      description= "Due time of the task in HH:MM format (default 12:00 AM)",
      option_type= 3,
      required=False
    ),
    create_option(
      name= "links",
      description= "Any associated links",
      option_type= 3,
      required=False
    )
  ])
async def _add_task(ctx: SlashContext, class_name: str, description: str, due_date: str, due_time: str = "12:00 AM", links: str = ""):
    print(f'{ctx.author.name} added a task for {class_name} which is due on {due_date} {due_time}. The task is to {description}.', flush=True)
    db.add_task(Task(class_name, description, due_date, due_time, links, ctx.author.name))
    await ctx.send(f'{ctx.author.name} added a task for {class_name} which is due on {due_date} {due_time}. The task is to {description}.')

@slash.slash(name="show_tasks", description="shows all the tasks added by a user")
async def _show_tasks(ctx: SlashContext):
    try:
      print(f'{ctx.author.name} wants to see all their tasks.')
      tasks = db.show_tasks_by_user(ctx.author.name)
      if len(tasks) == 0:
        await ctx.send(f'{ctx.author.name} has no tasks.')
      else:
        taskObjs = []
        [Task(x[0], x[1], x[2], x[3], x[4], x[5]) for x in tasks]
        await ctx.send("\n".join(taskObjs))
    except Exception as e:
      print(f"Error: {e}", flush=True)
      print("Command failed.", flush=True)


bot.run(TOKEN)