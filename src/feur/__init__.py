from injector import Injector

from feur.bot import Feur, BotModule
from feur.configuration import ConfigurationModule


def main():
    Injector([
        ConfigurationModule(),
        BotModule()
    ]).get(Feur).run()


if __name__ == "__main__":
    main()