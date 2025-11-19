import discord
import os
from dotenv import load_dotenv
import requests
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


# ---- Modal Definition ----
class ClaimModal(discord.ui.Modal, title="Claim Reward"):

    code = discord.ui.TextInput(
        label="Enter your claim code",
        placeholder="XYZ-123",
        required=True,
        max_length=50,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Thanks! You submitted: **{self.code.value}**",
            ephemeral=True
        )

@bot.command()
async def claim(ctx):
    print('Opening modal')
    """Opens the claim modal."""
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
