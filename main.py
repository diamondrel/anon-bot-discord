import os
import discord

discord_token_secret = os.environ['token']
bot = discord.Bot()

@bot.slash_command(guild_ids=[691127432165589013])
async def anon(ctx, text):
  channel = bot.get_channel(938277429720530954)
  await channel.send(text)
  await ctx.respond("Sent!", ephemeral=True)

bot.run(discord_token_secret)
