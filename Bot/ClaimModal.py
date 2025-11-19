import discord
from discord import ui
# ---- Modal Definition ----
class ClaimModal(ui.Modal, title="Claim Reward"):

    code = ui.TextInput(
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