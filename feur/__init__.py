import json
import logging
import sys
import re
import os
import random
import nextcord


class FeurBot(nextcord.Client):

    def __init__(self, token: str, answers: str, log_level: str):
        self.__token = token
        self.__logger = logging.getLogger("FeurBot")
        self.__logger.setLevel(logging.getLevelName(log_level))
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)
        self.__logger.info("Loading answers")
        answers_path = answers or os.path.join(os.path.dirname(__file__), "answers.json")
        self.__logger.info("Loading answers from %s", answers_path)
        with open(answers_path, "r") as answers_file:
            self.__answers = json.load(answers_file)
        self.__logger.info("Initializing bot...")
        intents = nextcord.Intents.default()
        intents.messages = True
        intents.message_content = True
        nextcord.Client.__init__(self, intents=intents)

    async def on_ready(self):
        self.__logger.info("Bot is ready")

    async def on_message(self, message: nextcord.Message):
        if message.author == self.user:
            self.__logger.debug("Received message from the bot, ignoring it")
            return
        self.__logger.debug("Received message : %s" % message.content)
        for handler in self.__answers["handlers"]:
            matcher = handler["matcher"]
            self.__logger.debug("Looking if message matches %s" % matcher)
            if re.search(matcher, message.content, re.IGNORECASE):
                if "secret_answer" in handler and random.randrange(1000) == 0:
                    answer = handler["secret_answer"]
                else:
                    answer = handler["answer"]
                self.__logger.debug("Handler matched, sending reply : %s" % answer)
                await message.reply(answer)
                break

    def run(self):
        self.__logger.info("Starting bot...")
        nextcord.Client.run(self, self.__token)
