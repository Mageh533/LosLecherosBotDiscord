import discord
import youtube_dl
import os
from discord.ext import commands
from discord import FFmpegPCMAudio

token = "ODk3OTExNDYxOTY2NDAxNTg2.YWcjNg.oEyCG0BQqIBODVKGKrjPt0OXWp0"
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
  print("Bot is now logged in as {0.user}".format(client))

@client.command(pass_context = True)
async def play(ctx, url : str):
  song_there = os.path.isfile("song.mp3")
  try:
    if song_there:
      os.remove("song.mp3")
  except PermissionError:
    await ctx.send("Ya hay una musica reproduciéndose")
    return

  ydl_opts = {
        'format': '249/250/251',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      await ctx.send("Cargando...")
      ydl._ies = [ydl.get_info_extractor('Youtube')]
      ydl.download([url])
    for file in os.listdir('./'):
      if file.endswith(".mp3"):
        filename = os.path.basename(file)
        os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send("Reproduciendo")
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