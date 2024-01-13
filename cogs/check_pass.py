from io import BytesIO

import discord
from PIL import Image
from discord import app_commands, File
from discord.ext import commands

from utils.create_image import resolve_stamps, add_stamps


class CheckPass(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="view_pass")
    async def token_list(self, interaction: discord.Interaction, user: discord.Member = None):
        await interaction.response.defer(ephemeral=False)
        if user is None:
            user = interaction.user

        profile_picture = user.avatar
        if profile_picture is None:
            profile_picture = user.default_avatar
        name = user.name
        user_roles: list = user.roles

        message = """
        Welcome to Ngmistan!
        Our immigration officers will check your passport and make sure you have a valid visa.
        If you don't, they will kindly ask you to leave and never come back.
        But if you do,well you gave lewis a lot of your lunch money!"""
        try:
            stamps = resolve_stamps(user_roles)
            data = BytesIO(await profile_picture.read())
            pfp = Image.open(data)

            passport = await add_stamps(stamps=stamps, user_name=name, avatar=pfp)
            await interaction.followup.send(message, file=File(passport))
        except Exception as e:
            print(e)
            await interaction.followup.send(f'error{e}')


async def setup(bot):
    await bot.add_cog(CheckPass(bot))
