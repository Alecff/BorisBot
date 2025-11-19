import discord
import os
import requests

from dotenv import load_dotenv
from discord.ext import commands
from Bot import ClaimModal

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def claim(ctx):
    # Opens the claim modal
    # Must defer to turn command message into an interaction
    await ctx.reply("Opening claim form...", delete_after=1)

    # Convert this context to an interaction using followup
    # Easiest approach: send a dummy button that opens the modal
    class OpenModalButton(discord.ui.View):
        @discord.ui.button(label="Open Claim Form", style=discord.ButtonStyle.primary)
        async def open(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_modal(ClaimModal())

    await ctx.send("Click below to enter your claim:", view=OpenModalButton())

bot.run(os.environ.get('TOKEN'))
