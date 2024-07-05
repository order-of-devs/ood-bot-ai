# This example requires the 'message_content' intent.

import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.tree.command(name="paa",description="hello world command")
async def papa(interaction):
    await interaction.response.send_message("Hello, World!")


@bot.event
async def on_ready():
    print(f'Logged on as!')
    guild = discord.Object(871795158608404530)

    await bot.tree.sync(guild=guild)

bot.run('token')
