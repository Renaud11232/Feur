import nextcord
from nextcord.ext import commands

from injector import Module, singleton, provider

from feur.bot.cogs import *


class BotModule(Module):

    @singleton
    @provider
    def provide_bot(self,
                    ready_listener: ReadyListener,
                    message_listener: MessageListener) -> commands.Bot:
        intents = nextcord.Intents.default()
        intents.messages = True
        intents.message_content = True
        bot =  commands.Bot(
            intents=intents
        )
        bot.add_cog(ready_listener)
        bot.add_cog(message_listener)
        return bot
