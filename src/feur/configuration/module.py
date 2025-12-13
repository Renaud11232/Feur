import argparse
import logging

from injector import Module, singleton, provider

from .configuration import Configuration
from .action import EnvDefault


class ConfigurationModule(Module):

    @singleton
    @provider
    def provide_configuration(self) -> Configuration:
        parser = argparse.ArgumentParser(description='Starts the FeurBot')
        parser.add_argument(
            "--discord-token",
            action=EnvDefault,
            type=str,
            required=True,
            env_var="DISCORD_TOKEN",
            help="Bot token used to access Discord API. If omitted, the value of the `DISCORD_TOKEN` environment variable will used."
        )
        parser.add_argument(
            "--log-level",
            action=EnvDefault,
            type=str,
            required=True,
            default="INFO",
            env_var="LOG_LEVEL",
            choices=logging.getLevelNamesMapping().keys(),
            help="Log level. If omitted, the value of the `LOG_LEVEL` environment variable will be used. Defaults to `INFO`"
        )
        parser.add_argument(
            "--answers",
            action=EnvDefault,
            type=str,
            required=False,
            env_var="ANSWERS",
            help="Path to the answers definition file. If omitted, the value of the `ANSWERS` environment variable will used."
        )
        args = parser.parse_args()
        return Configuration(
            discord_token=args.discord_token,
            log_level=args.log_level,
            answers=args.answers
        )
