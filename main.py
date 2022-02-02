import os
discord_token_secret = os.environ['token'] 
channel_name_secret = os.environ['channel'] 
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
client = commands.Bot(command_prefix='!')
slash = SlashCommand(client, sync_commands=True)

@slash.slash(
  name="anon",
  description="Sends a Message Anonymously",
  guild_ids=[691127432165589013],
  options=[
    create_option(
      name="text",
      description="Enter Text",
      required=True,
      option_type=3
    )
  ]
)

async def _hello(ctx:SlashContext, text:str):
  await client.wait_until_ready()
  print(client)
  print("\n")
  print(channel_name_secret)
  print(text)
  print("\n")
  await channel.send(text)
  await ctx.send("Sent!",hidden=True,)

client.run(discord_token_secret)
