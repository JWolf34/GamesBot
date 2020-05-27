#! python3

import os
import discord
from discord.ext import commands
import json

with open('config.json') as config_file:
    data = json.load(config_file)

TOKEN = data['discord-token']

client = commands.Bot(command_prefix='./')


@client.event
async def on_ready():
    print('Connected!')


@client.event
async def on_member_join(member):
    print(f'Bring back {member}... whats the point?')


client.run(TOKEN)
