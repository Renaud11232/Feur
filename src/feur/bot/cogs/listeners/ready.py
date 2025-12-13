import logging

from injector import singleton, inject

from nextcord.ext import commands

from feur.bot.services import BotService


@singleton
class ReadyListener(commands.Cog):

    @inject
    def __init__(self, bot_service: BotService):
        super().__init__()
        self.__bot_service = bot_service
        self.__logger = logging.getLogger("feur.listeners.ready")

    @commands.Cog.listener()
    async def on_ready(self):
        self.__logger.debug("Handling ready event")
        self.__bot_service.on_ready()
        self.__logger.debug("Successfully handled ready event")