from dataclasses import dataclass


@dataclass
class Configuration:
    discord_token: str
    log_level: int
    answers: str | None