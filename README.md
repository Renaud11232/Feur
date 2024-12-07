# Feur

Feur is a simple bot that was created for a stupid joke.

This bot was designed to replay to messages matching "Quoi" with "Feur". However, you can configure it to reply to any
message matching a regular expression with a custom message.

This also works with direct messages to the bot.

The docker images can be used on `amd64` and `arm64` systems.

## Starting the bot

You can run this bot using docker CLI, docker-compose or directly on your machine once the python package is installed.

### Parameters

The arguments the bot accepts can be set using a command line flag or using environment variables.
If the same option is set using both the command line flag and environment variable, the environment variable will be
ignored.

| CLI flag          | Environment variable | Description                                                                                                 | Required | Default        |
|-------------------|----------------------|-------------------------------------------------------------------------------------------------------------|----------|----------------|
| `--discord-token` | `DISCORD_TOKEN`      | The Discord bot token used to access the Discord API                                                        | Yes      |                |
| `--log-level`     | `LOG_LEVEL`          | The log level of the bot.                                                                                   | No       | `INFO`         |
| `--answers`       | `ANSWERS`            | The path to the answers.json file that contains regex to match messages and the answer for matched messages | No       | `answers.json` |


### Docker CLI

```bash
docker run \
  -d \
  --name feur \
  --restart unless-stopped \
  -e DISCORD_TOKEN=yourtoken \
  -e LOG_LEVEL=INFO \
  -e ANSWERS=/answers.json \
  ghcr.io/renaud11232/feur
```

### Docker compose

`compose.yaml`:

```yml
services:
  feur:
    image: ghcr.io/renaud11232/feur
    restart: unless-stopped
    environment:
      DISCORD_TOKEN: yourtoken
      LOG_LEVEL: INFO
      ANSWERS: /answers.json
```

```bash
docker-compose up -d
```

### Bare metal

You can install this bot by running the following command (a venv is recommended) :

```bash
pip install "https://github.com/Renaud11232/Feur/archive/refs/heads/master.zip"
```

Once it's installed you can start it either by setting the environment variables :
```bash
export DISCORD_TOKEN=yourtoken
export LOG_LEVEL=INFO
export ANSWERS=/answers.json
feur
```

Or by providing the correct flags :
```bash
feur \
  --discord-token yourtoken \
  --log-level INFO \
  --answers /answers.json
```