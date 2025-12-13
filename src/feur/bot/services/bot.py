import logging

import nextcord
from nextcord.ext import commands

from injector import singleton, inject, ProviderOf


@singleton
class BotService:

    @inject
    def __init__(self, bot_provider: ProviderOf[commands.Bot]):
        self.__bot_provider = bot_provider
        self.__logger = logging.getLogger("feur.bot")

    def on_ready(self):
        scopes = [
            "bot"
        ]
        permissions = nextcord.Permissions.none()
        permissions.update(
            read_messages=True
        )
        invite_url = nextcord.utils.oauth_url(
            self.__bot_provider.get().user.id,
            scopes=scopes,
            permissions=permissions
        )
        self.__logger.info(f"Feur is ready ! You can invite the bot with {invite_url}")
