import asyncio
import aiohttp
import datetime
from config import open_weather_token

code_to_smile = {
    "Clear": "Ясно \U00002600",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U00002614",
    "Drizzle": "Дождь \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U0001F32B"
}

async def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                data = await response.json()

        if str(data.get("cod", "")) != "200":
            return {"error": data.get("message", "Ошибка API")}

        weather_description = data["weather"][0]["main"]
        wd = code_to_smile.get(weather_description, "Погода неизвестна")

        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": wd,
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind": data["wind"]["speed"],
            "sunrise": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]),
            "sunset": datetime.datetime.fromtimestamp(data["sys"]["sunset"]),
        }
        result["day_length"] = result["sunset"] - result["sunrise"]
        return result

    except asyncio.TimeoutError:
        return {"error": "Проблема с сетью или API"}
    except Exception:
        return {"error": "Произошла непредвиденная ошибка"}