from injector import inject, singleton

import discord
from discord.ext import commands

from feur.bot.cogs import *


@singleton
class FeurBot(commands.Bot):

    @inject
    def __init__(self, ready_listener: ReadyListener,
                       message_listener: MessageListener):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        super().__init__(
            intents=intents,
            command_prefix=[],
            help_command=None
        )
        self.__feur_cogs = [
            ready_listener,
            message_listener
        ]

    async def setup_hook(self) -> None:
        for cog in self.__feur_cogs:
            await self.add_cog(cog)
