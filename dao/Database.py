import pymysql

import configparser
import os


dao_dir = os.path.dirname(os.path.abspath(__file__))
cfg_path = os.path.join(dao_dir, "../resources/config.ini")

cfg = configparser.ConfigParser()
cfg.read(cfg_path)


class Database:
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host=cfg.get("mysql", "host"),
            port=int(cfg.get("mysql", "port")),
            user=cfg.get("mysql", "user"),
            password=cfg.get("mysql", "password"),
            db=cfg.get("mysql", "db"),
            charset=cfg.get("mysql", "charset"),
            cursorclass=pymysql.cursors.DictCursor,
        )
        # self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
