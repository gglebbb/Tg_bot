from dataclasses import dataclass
from typing import List

from environs import Env


@dataclass
class TgBot:
    token: str
    admins_ids: List[int]
    use_redis: bool


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class Miscellaneous:
    other_parament: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path=path)
    return Config(
        tg_bot=TgBot(token=env.str("BOT_TOKEN"),
                     admins_ids=list((int, env.list("ADMINS"))),
                     use_redis=env.bool("USE_REDIS")),
        db=DbConfig(host=env.str("DB_HOST"),
                    password=env.str("DB_PASSWORD"),
                    user=env.str("DB_USER"),
                    database=env.str("DB_NAME")),
        misc=Miscellaneous()
    )
