import discord
from discord.ext import commands

token = "ODk3OTExNDYxOTY2NDAxNTg2.YWcjNg.oEyCG0BQqIBODVKGKrjPt0OXWp0"
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print("Bot is now logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return
  
  if message.content.startswith("Quien es paco?"):
    await message.channel.send("El mejor bot del mundo creado por el mejor programador lechero que existe")

@client.command(pass_context = True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("Oye tonto que tal si entras en un canal de voz antes de usar ese comando?")

@client.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Deu")
  else:
    await ctx.send("No estoy en ningun canal de voz")

client.run(token)