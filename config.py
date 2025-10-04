import os
from dotenv import load_dotenv

load_dotenv()

class Configuration:
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB = os.getenv("MONGO_DB")
    
    BCB_API_MENSAL = os.getenv("BCB_API_MENSAL")
    BCB_API_SELIC = os.getenv("BCB_API_SELIC")
    BCB_API_TRIMESTRAL = os.getenv("BCB_API_TRIMESTRAL")
    BCB_API_ANUAL = os.getenv("BCB_API_ANUAL")