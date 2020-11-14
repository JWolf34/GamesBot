#! python3

import os
import discord
from discord.ext import commands
import asyncio
import json
import RedditGamesScraper

with open('config.json') as config_file:
    data = json.load(config_file)

TOKEN = data['discord'][0]['token']

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Connected!')


async def getGameNews():
    await client.wait_until_ready()

    try:
        channel = client.get_channel(710714643437453315)
        games = RedditGamesScraper.RedditGamesScraper()
        while not client.is_closed():
            links = games.getLinks()
            for link in links:
                embed = discord.Embed(
                    title=link.title, url="https://reddit.com" + link.permalink)
                await channel.send(embed=embed)
                await asyncio.sleep(1)
            await asyncio.sleep(300)
    except Exception as e:
        channel.send("I can't send games news right now :( \n" + e)




client.loop.create_task(getGameNews())
client.run(TOKEN)
