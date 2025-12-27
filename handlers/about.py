from aiogram import types

async def about_command(message: types.Message):
    await message.answer(
        "ℹ️ Этот бот показывает погоду в любом городе мира.\n"
        "Данные берутся с OpenWeather API.\n"
        "Можно выбрать город кнопкой или ввести название вручную.\n"
    )