import logging

from injector import singleton, inject, ProviderOf
import nextcord
from nextcord.ext import commands

from feur.bot.services.answers import AnswersService


@singleton
class MessageService:

    @inject
    def __init__(self, answers_service: AnswersService, bot_provider: ProviderOf[commands.Bot]):
        self.__answers_service = answers_service
        self.__bot_provider = bot_provider
        self.__logger = logging.getLogger("feur.message")

    async def handle(self, message: nextcord.Message):
        if message.author.id == self.__bot_provider.get().user.id:
            self.__logger.debug(f"Received message from the bot, ignoring it")
            return
        self.__logger.debug(f"Received message : {message.content}")
        answer = self.__answers_service.get_answer(message.content)
        if answer is not None:
            await message.reply(answer)