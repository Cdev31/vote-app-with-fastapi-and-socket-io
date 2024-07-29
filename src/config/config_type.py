from typing import TypedDict



class ConfigType( TypedDict ):
    db_url: str
    secret_key: str
    algorithm: str
