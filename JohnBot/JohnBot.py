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


async def getGamesNews():
    await client.wait_until_ready()

    try:
        channel = client.get_channel(710714643437453315)
        games = RedditGamesScraper.RedditGamesScraper()
        while not client.is_closed():
            links = games.getLinks(0.78, 850)
            for link in links:
                embed = discord.Embed(
                    title=link.title, url="https://reddit.com" + link.permalink)
                await channel.send(embed=embed)
                await asyncio.sleep(1)
            await asyncio.sleep(300)
    except Exception as e:
        channel.send("Could not crawl (General Exception): " + e.toString())


async def getPCSales():
    await client.wait_until_ready()

    channel = client(777046244127408139)

client.loop.create_task(getGameNews(0.78, 850, ))
client.loop.create_task(getPCSales())
client.run(TOKEN)
