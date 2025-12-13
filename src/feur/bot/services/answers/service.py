import logging
import os
import json
import re
import random

from injector import singleton, inject

from feur.configuration import Configuration


@singleton
class AnswersService:

    @inject
    def __init__(self, configuration: Configuration):
        self.__logger = logging.getLogger("feur.answers")
        answers_path = configuration.answers or os.path.join(os.path.dirname(__file__), "answers.json")
        with open(answers_path, "r", encoding="utf8") as answers_file:
            self.__answers = json.load(answers_file)

    def get_answer(self, message_content: str) -> str | None:
        self.__logger.debug(f"Checking for possible answers...")
        for handler in self.__answers["handlers"]:
            matcher = handler["matcher"]
            self.__logger.debug(f"Checking if {message_content} matches {matcher}")
            if re.search(matcher, message_content, re.IGNORECASE):
                if "secret_answer" in handler and random.randrange(1000) == 0:
                    answer = handler["secret_answer"]
                else:
                    answer = handler["answer"]
                self.__logger.debug(f"Handler matched, returning reply : {answer}")
                return answer
        return None