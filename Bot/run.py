import discord
import os
import requests
import ClaimModal

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def claim(ctx):
    # Must defer to turn command message into an interaction
    await ctx.reply("Opening claim form...", delete_after=1)

    # Convert this context to an interaction using followup
    # Easiest approach: send a dummy button that opens the modal
    class OpenModalButton(discord.ui.View):
        @discord.ui.button(label="Open Claim Form", style=discord.ButtonStyle.primary)
        async def open(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_modal(ClaimModal.ClaimModal())

    await ctx.send("Click below to enter your claim:", view=OpenModalButton())

bot.run(os.environ.get('TOKEN'))
