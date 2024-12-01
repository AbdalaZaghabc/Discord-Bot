import discord
from discord.ext import commands
import os, asyncio

# import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

# remove the default help command so that we can write our own
bot.remove_command('help')

# Function to read the token from a file
def get_token_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().strip()

async def main():
    token = get_token_from_file('token.txt')  # Replace 'token.txt' with your token file path
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(token)

asyncio.run(main())