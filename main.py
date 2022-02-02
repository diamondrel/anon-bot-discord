import os
import yaml
yamFile = yaml.load(open('/.github/workflows/github-actions-demo.yaml'))
yamFileTwo = yaml.load(open('/.github/workflows/database.yaml'))
discord_token_secret = yamFile['jobs']['build']['steps']['env']['token']
channel_name_secret = yamFile['jobs']['build']['steps']['env']['channel']
discord_token_better = yamFileTwo['database']['env']['token']
channel_name_better = yamFileTwo['database']['env']['channel']
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
  channel = client.get_channel(channel_name_secret)
  await channel.send(text)
  await ctx.send("Sent!",hidden=True,)

client.run(discord_token_secret)
