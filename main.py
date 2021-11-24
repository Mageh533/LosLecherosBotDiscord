import discord
import os
from pytube import YouTube
from discord.ext import commands
from discord import FFmpegPCMAudio

token = os.environ['DISCORD_TOKEN']
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

  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    name = YouTube(url).title
    YouTube(url).streams.get_audio_only().download(filename='song.mp3')
    for file in os.listdir('./'):
      if file.endswith(".mp3"):
        filename = os.path.basename(file)
        os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send("Reproduciendo " + name)
  else:
    await ctx.send("Oye tonto que tal si entras en un canal de voz antes de usar ese comando?")

@client.command(pass_context = True)
async def stop(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Deu")
  else:
    await ctx.send("No estoy en ningun canal de voz")

@client.command(pass_context = True)
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
    await ctx.send("Pausando")
  else:
    await ctx.send("Ya esta pausado")

@client.command(pass_context = True)
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_paused():
    voice.resume()
    await ctx.send("Reanuando")
  else:
    await ctx.send("Ya esta reproduciéndose")

@client.command(pass_context = True)
async def speak(ctx):
  channel = ctx.message.author.voice.channel
  voice = await channel.connect()
  voice.play(discord.FFmpegPCMAudio("audios/voz.mp3"))


client.run(token)
