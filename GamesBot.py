#! python3

import os
import discord
from discord.ext import commands
import json
import RedditGamesScraper

with open('config.json') as config_file:
    data = json.load(config_file)

TOKEN = data['discord'][0]['token']

client = commands.Bot(command_prefix='./')


@client.event
async def on_ready():
    print('Connected!')
    getNews()


@client.event
async def on_member_join(member):
    print(f'Bring back {member}... whats the point?')


def getNews():
    games = RedditGamesScraper.RedditGamesScraper()
    links = games.getLinks()
    print(links)


client.run(TOKEN)
