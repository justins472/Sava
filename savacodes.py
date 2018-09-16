import discord
from discord.ext import commands

TOKEN = 'NDkwNjIzMzk3NDU0MTUxNjgx.Dn8I-A.H7N23wPrBzDPErwYCImImxxuo1M'

client = commands.Bot(command_prefix='?')
client.remove_command('help')

@client.event
async def on_ready():
 print('Ready')

@client.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name='Unknown Error!', value='```There was an unknown error!\n We will report this to the staff team ASAP!```', inline=False)
        await client.send_message(channel, embed=embed)
       
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=0xff00e6)
    embed.set_author(name='SavaBot Help!')
    embed.add_field(name='Current Status:', value='We are currently working on the bot Sorry!', inline=False)
    await client.say(embed=embed)
   

 
client.run(TOKEN)
