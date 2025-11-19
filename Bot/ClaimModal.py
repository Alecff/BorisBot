import discord
from discord import ui
from testRequest import createClaim

# ---- Modal Definition ----
class ClaimModal(ui.Modal, title="Claim Reward"):

    email = ui.TextInput(
        label="Enter your email address",
        placeholder="test@test.com",
        required=True,
        max_length=50,
    )

    async def on_submit(self, interaction: discord.Interaction):
        ref = createClaim(self.email.value, interaction.user.display_name)
        await interaction.response.send_message(
            f"Thanks! Your claim ref is: {ref}",
            ephemeral=True
        )
