import discord

from discord.ext import commands
from discord.ext import tasks

import json
import os
import asyncio



import random
from random import choice
from random import seed
from random import randint




TOKEN = "ODkwNTk2NjUyODA3NzgyNDUx.YUyGxA.qUOpsG0iejeeuqxlvuRzvLdjnGQ"

client = commands.Bot(command_prefix=commands.when_mentioned_or('dala ', 'dala'), help_command = None)


@client.event
async def on_ready():
    print('dala')




#dance gif
@client.command()
async def dance(ctx):

  dance=("https://c.tenor.com/RjG1C44wSacAAAAC/psoriasis-adichi.gif", "https://c.tenor.com/ym_xkFhGXHEAAAAC/podu-funny.gif",
   "https://c.tenor.com/v5cMs2leUqYAAAAC/ajith-thala.gif", "https://c.tenor.com/7rzPaysny4kAAAAC/funny-ajith.gif",
    "https://tenor.com/view/ajithdance-ajith-dalaajith-gif-18009062", "https://c.tenor.com/PVVKR5oJMQcAAAAC/ajith-thala-citizen.gif",
    "https://cdn.discordapp.com/attachments/873932495119339530/895557189895344138/16335878653717065697068374114271.gif")

    
  await ctx.reply(random.choice(dance))


#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round(client.latency * 1000)}`ms')

#leveling system
with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass
 
with open('users.json', 'r') as f:
  users = json.load(f)
 
@client.event    
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_experience(users, message.author)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)
            await client.process_commands(message)
 
async def add_experience(users, user):
  if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
  users[f'{user.id}']['experience'] += 6
  print(f"{users[f'{user.id}']['level']}")
 
async def level_up(users, user, message):
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 4))
  if lvl_start < lvl_end:
    await message.channel.send(f':tada: {user.mention} has reached level {lvl_end}. Congrats! :tada:')
    users[f'{user.id}']["level"] = lvl_end
 
@client.command()
async def rank(ctx, member: discord.Member = None):
  if member == None:
    userlvl = users[f'{ctx.author.id}']['level']
    await ctx.send(f'{ctx.author.mention} You are at level {userlvl}!')
  else:
    userlvl2 = users[f'{member.id}']['level']
    await ctx.send(f'{member.mention} is at level {userlvl2}!')






client.run(TOKEN)