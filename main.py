import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Import other necessary modules

# Load .env and initialize bot
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
initial_extensions = [
    'cogs.meme_cog',  # Import other cog modules here
]

for extension in initial_extensions:
    client.load_extension(extension)

# Slash command decorator
@client.slash_command()
async def gen(ctx, prompt: str):
    # Your slash command implementation here

# Start the bot
client.run(bot_token)

