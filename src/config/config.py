import os
from dotenv import load_dotenv
from .config_type import ConfigType

load_dotenv() 


config: ConfigType = {
    'db_url': os.getenv('DB_URL') or '',
    'secret_key': os.getenv('SECRET_KEY') or '',
    'algorithm': os.getenv("ALGORITHM") or ''
}
