from dotenv import load_dotenv
import os

load_dotenv()  # загружаем .env

tg_bot_token = os.getenv("TG_BOT_TOKEN")
open_weather_token = os.getenv("OPEN_WEATHER_TOKEN")