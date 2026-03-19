import logging

from injector import singleton, inject

import discord
from discord.ext import commands

from feur.bot.services import MessageService


@singleton
class MessageListener(commands.Cog):

    @inject
    def __init__(self, message_service: MessageService):
        super().__init__()
        self.__message_service = message_service
        self.__logger = logging.getLogger("feur.listeners")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        self.__logger.debug(f"Handling message event")
        await self.__message_service.handle(message)
        self.__logger.debug("Successfully handled message event")