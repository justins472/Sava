import discord
from discord.ext import commands

TOKEN = 'NDkwNjIzMzk3NDU0MTUxNjgx.Dn8I-A.H7N23wPrBzDPErwYCImImxxuo1M'

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
 print('Ready')

@client.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Unknown Error!', value='```There was an unknown error! We will report this to the staff team ASAP!', inline=False)
        await client.send_message(channel, embed=embed)

 
client.run(TOKEN)
