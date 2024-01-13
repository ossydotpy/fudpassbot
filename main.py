from typing import Optional, Literal

import discord
import os, asyncio

from discord import app_commands, Activity, ActivityType
from discord.ext import commands
from discord.ext.commands import Context, Greedy

from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
TOKEN = os.getenv("PASSBOT")

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{datetime.now()} | Bot {bot.application_id} has logged in .")
    await bot.change_presence(
        activity=Activity(type=ActivityType.watching, name="dee's mom")
    )
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"{datetime.now()} | {filename[:-3]} loaded successfully.")
            except Exception as e:
                print(f"{datetime.now()} | Error loading {filename}: {e}")


@bot.command(hidden=True)
@commands.guild_only()
@commands.is_owner()
async def sync(
    ctx: Context,
    guilds: Greedy[discord.Object],
    spec: Optional[Literal["~", "*", "^"]] = None,
) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"{datetime.now()} | Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        print(
            f"{datetime.now()} | Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return


async def main():
    await bot.start(TOKEN)


asyncio.run(main())
