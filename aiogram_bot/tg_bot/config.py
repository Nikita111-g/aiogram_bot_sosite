from dataclasses import dataclass
from typing import List
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_ids: List[int]

@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig 
    

def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env.str('BOT_TOKEN'),
            admin_ids=env.list('ADMINS')
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASSWORD'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        )
    )

