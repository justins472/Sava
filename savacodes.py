import discord
from discord.ext import commands

TOKEN = 'NDkwNjIzMzk3NDU0MTUxNjgx.Dn8I-A.H7N23wPrBzDPErwYCImImxxuo1M'

client = commands.Bot(command_prefix='?')

if(cmd == ${prefix}hello{
    message.reply"Hello!"
})

@client.event
async def on_ready():
    print('Ready')

client.run(TOKEN)
