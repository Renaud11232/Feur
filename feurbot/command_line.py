import argparse
import os

from feurbot import FeurBot


def main():
    parser = argparse.ArgumentParser(description='Starts the FeurBot')
    parser.add_argument("--discord-token",
                        type=str,
                        default=os.environ.get("DISCORD_TOKEN"),
                        help="Bot token used to access Discord API. If omitted, the value of the `DISCORD_TOKEN` environment variable will used."
                        )
    parser.add_argument("--log-level",
                        type=str,
                        default=os.environ.get("LOG_LEVEL") or "INFO",
                        help="Log level. If omitted, the value of the `LOG_LEVEL` environment variable will be used. Defaults to `INFO`"
                        )
    parser.add_argument("--answers",
                        type=str,
                        default=os.environ.get("ANSWERS") or "answers.json",
                        help="Path to the answers definition file. If omitted, the value of the `ANSWERS` environment variable will used."
                        )
    args = parser.parse_args()
    bot = FeurBot(args.discord_token, args.answers, args.log_level)
    bot.run()

if __name__ == "__main__":
    main()