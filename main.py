import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

token = "ODk3OTExNDYxOTY2NDAxNTg2.YWcjNg.oEyCG0BQqIBODVKGKrjPt0OXWp0"
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
  print("Bot is now logged in as {0.user}".format(client))

@client.command(pass_context = True)
async def play(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('audio/Ameno.mp3')
    player = voice.play(source)
  else:
    await ctx.send("Oye tonto que tal si entras en un canal de voz antes de usar ese comando?")

@client.command(pass_context = True)
async def stop(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Deu")
  else:
    await ctx.send("No estoy en ningun canal de voz")

client.run(token)