import discord
from discord.ext import commands as discord_commands

from src.bot.commands.ask_ai_command import AskAICommand
from src.bot.commands.summarize_command import SummarizeCommand
from src.core.config import Settings

OWNER_USERID = 411490244660166656


class DiscordBot:
    def __init__(self, settings: Settings):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = discord_commands.Bot(command_prefix="/", intents=intents)
        self.ask_ai_command = AskAICommand()
        self.summarize_command = SummarizeCommand()
        self.discord_token = settings.discord_token

    def __call__(self, *args, **kwargs):
        @self.bot.tree.command(name="ask_ai", description="ask ai command")
        async def ask_ai(interaction):
            await self.ask_ai_command.execute(interaction.data)
            await interaction.response.send_message("Exterminate! Exterminate!")

        @self.bot.tree.command(name="summarize", description="summarize")
        async def summarize(interaction):
            await self.summarize_command.execute(interaction.data)
            await interaction.response.send_message("Summarization started!")

        @self.bot.command()
        async def sync(ctx):
            print("sync command")
            if ctx.author.id == OWNER_USERID:
                guild = discord.Object(871795158608404530)
                self.bot.tree.copy_global_to(guild=guild)
                await self.bot.tree.sync(guild=guild)
                await self.bot.tree.sync()
                await ctx.send("Command tree synced.")
            else:
                await ctx.send("You must be the owner to use this command!")

        # @self.bot.event
        # async def on_message():
        #     pass
        #     # await message.add_reaction('👍')
        #     # await self.bot.process_commands(message)

        @self.bot.event
        async def on_ready():
            print("Logged on as!")

        self.bot.run(self.discord_token)
