import dotenv
import pathlib
import os
from bot import services

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
dotenv.load_dotenv(str(BASE_DIR) + "/.env")
TOKEN = os.getenv("BOT_TOKEN")
PRICE_LIST = services.read_price_list(str(BASE_DIR) + "/prices.json")
DIALOG_SCENARIO = services.get_dialog_scenario(str(BASE_DIR) + "/user_scenario.yaml")
