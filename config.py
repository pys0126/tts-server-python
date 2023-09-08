import os
from configparser import ConfigParser, SectionProxy

CONFIG_PATH: str = "./config.ini"
config: ConfigParser = ConfigParser()
config_name: str = "AppConfig"

# 如果配置文件不存在则创建一个
if not os.path.exists(CONFIG_PATH):
    config[config_name]: dict = {
        "host": "0.0.0.0",
        "port": 8000,
        "workers": 4,
        "cache_path": "./cache"
    }
    with open(CONFIG_PATH, "w", encoding="u8") as f:
        config.write(f)

config.read(CONFIG_PATH)
app_config: SectionProxy = config[config_name]

host: str = app_config.get("host")
port: int = int(app_config.get("port"))
workers: int = int(app_config.get("workers"))
cache_path: str = app_config.get("cache_path")