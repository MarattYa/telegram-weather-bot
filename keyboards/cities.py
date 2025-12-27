from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def popular_cities_keyboard():
    cities = ["Moscow", "London", "Paris", "New York", "Tokyo", "Berlin"]
    buttons = [InlineKeyboardButton(text=city, callback_data=city.lower().replace(" ", "_")) for city in cities]
    keyboard_rows = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)