from dataclasses import dataclass


@dataclass
class Configuration:
    discord_token: str
    log_level: str
    answers: str | None