from datetime import UTC, datetime, timedelta
from typing import Any

import discord
from discord.ext import commands as discord_commands

from src.asserts import is_number
from src.bot.commands.ask_ai_command import AskAICommand
from src.bot.commands.summarize_command import SummarizeCommand
from src.core.config import Settings


class DiscordBot:
    def __init__(self, settings: Settings,
                 ask_ai_command: AskAICommand,
                 summarize_command: SummarizeCommand) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = discord_commands.Bot(command_prefix="/", intents=intents)
        self.ask_ai_command = ask_ai_command
        self.summarize_command = summarize_command
        self.discord_token = settings.discord_token
        self.owner_userid = settings.owner_userid
        self.guild_id = settings.guild_id

    def register_commands(self) -> None:
        @self.bot.tree.command(name="ask_ai", description="ask ai command")
        async def ask_ai(interaction: Any) -> None:
            await self.ask_ai_command.execute(interaction.data)
            await interaction.response.send_message("Exterminate! Exterminate!")

        @self.bot.tree.command(name="summarize", description="summarize")
        async def summarize(interaction: Any) -> None:
            await self.summarize_command.execute(interaction.data)
            await interaction.response.send_message("Summarization started!")

        @self.bot.tree.command(name="get_messages", description="get messages from a channel for the last x days")
        async def get_messages(interaction: Any, channel_id: str, days: int = 1) -> None:
            if interaction.user.id == self.owner_userid:
                if not is_number(channel_id):
                    await interaction.response.send_message("Invalid channel ID.")
                    return

                channel = self.bot.get_channel(int(channel_id))
                if not channel:
                    await interaction.response.send_message("Channel not found.")
                    return

                end_date = datetime.now(tz=UTC)
                start_date = end_date - timedelta(days=days)

                messages = [
                    f"{message.created_at}: {message.author}: {message.content}"
                    async for message in channel.history(limit=None, after=start_date, before=end_date)
                ]

                output_message = f"Got {len(messages)} messages from the last {days} days."
                await interaction.response.send_message(output_message)
            else:
                await interaction.response.send_message("You must be the owner to use this command!")

        @self.bot.command()
        async def sync(ctx: Any) -> None:
            if ctx.author.id == self.owner_userid:
                guild = discord.Object(self.guild_id)
                self.bot.tree.copy_global_to(guild=guild)
                await self.bot.tree.sync(guild=guild)
                await self.bot.tree.sync()
                await ctx.send("Command tree synced.")
            else:
                await ctx.send("You must be the owner to use this command!")

    def __call__(self) -> None:
        self.bot.run(self.discord_token)
