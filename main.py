import discord
from discord.ext import commands
from discord import app_commands
from flask import Flask
from threading import Thread
import os
import keep_alive
keep_alive.keep_alive()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
  
@bot.command()
async def bonjour(ctx):
  await ctx.send(f"Bonjour {ctx.author} !")

@bot.command()
async def cava(ctx):
  await ctx.send(f"Ça va et toi {ctx.author} ")

@bot.command()
async def minecraft(ctx):
  await ctx.send(f"block block !")

@bot.command()
async def easteregg(ctx):
  await ctx.send(f"Vous avez trouvé un easter egg !")   

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Project Horizon"))
  print(f'Connecté en tant que {bot.user}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='général')
    if channel:
        await channel.send(f'Bienvenue {member.mention} !')

Token = os.environ['TOKEN_BOT_DISCORD']
bot.run(Token)