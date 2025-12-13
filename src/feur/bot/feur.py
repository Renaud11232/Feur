import logging
import sys

from nextcord.ext import commands

from injector import inject, singleton

from feur.configuration import Configuration


@singleton
class Feur:

    @inject
    def __init__(self, configuration: Configuration, bot: commands.Bot):
        self.__configuration = configuration
        self.__bot = bot
        self.__init_logger("nextcord")
        self.__init_logger("feur")

    def __init_logger(self, name: str):
        logger = logging.getLogger(name)
        logger.setLevel(self.__configuration.log_level)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

    def run(self):
        self.__bot.run(self.__configuration.discord_token)