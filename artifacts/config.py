import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
LOCALIZE = os.getenv("LOCALIZE")
DEBUG = os.getenv("DEBUG")
LOG_PATH = os.getenv("LOG_PATH")
ARTIFACTS_DATA = os.getenv("ARTIFACTS_DATA")