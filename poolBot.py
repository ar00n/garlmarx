import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import urllib.request
import json
from time import sleep

bot = commands.Bot(command_prefix=')')

async def my_background_task():
    await bot.wait_until_ready()
    while True:
        url = 'http://garlmarx.fun/api/stats'
        req = urllib.request.Request(url)
        r = urllib.request.urlopen(req).read()
        a = json.loads(r.decode('utf-8'))
        hashRate = a["algos"]["allium"]["hashrate"]
        hashRate = hashRate / 1000000
        hashRate = str(hashRate)[:-14]
        hashRate = hashRate + ' MH/s'
        print(hashRate)
        await bot.change_presence(game=discord.Game(name=hashRate))
        await asyncio.sleep(60)

@bot.event
async def on_ready():
    print (bot.user.name + ' is ready')

bot.loop.create_task(my_background_task())
bot.run("NDE3OTUzNzQ5MTk4MTc2MjU3.DXahYw.4gfbykmLXqCAaWuhBtWdffishus")