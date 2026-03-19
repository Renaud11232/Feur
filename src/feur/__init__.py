from injector import Injector

from feur.app import Feur
from feur.bot import BotModule
from feur.configuration import ConfigurationModule


def main():
    Injector([
        ConfigurationModule(),
        BotModule()
    ]).get(Feur).run()


if __name__ == "__main__":
    main()