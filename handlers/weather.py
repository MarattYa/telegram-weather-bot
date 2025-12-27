from aiogram import types
from services.weather_service import get_weather

async def handle_city(city: str, send_to: types.Message):
    data = await get_weather(city)
    if "error" in data:
        await send_to.answer(f"☠ {data['error']} ☠")
    else:
        await send_to.answer(
            f"{data['city']}\n"
            f"{data['description']} 🌡 {data['temperature']}°C\n"
            f"Влажность: {data['humidity']}%\n"
            f"Давление: {data['pressure']} hPa\n"
            f"Ветер: {data['wind']} м/с\n"
            f"Восход: {data['sunrise'].strftime('%H:%M')}\n"
            f"Закат: {data['sunset'].strftime('%H:%M')}\n"
            f"Длительность дня: {data['day_length']}\n"
        )

async def message_handler(message: types.Message):
    city = message.text.strip()
    await handle_city(city, message)

async def callback_handler(callback: types.CallbackQuery):
    city = callback.data
    await handle_city(city, callback.message)
    await callback.answer()