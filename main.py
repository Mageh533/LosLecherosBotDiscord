import discord

token = "ODk3OTExNDYxOTY2NDAxNTg2.YWcjNg.oEyCG0BQqIBODVKGKrjPt0OXWp0"
client = discord.Client()

@client.event
async def on_ready():
  print("Bot is now logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return
  
  if message.content.startswith("-play"):
    await message.channel.send("Playing music")

client.run(token)