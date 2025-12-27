import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from config import tg_bot_token
from handlers import (
    start_command,
    help_command,
    about_command,
    message_handler,
    callback_handler
)


bot = Bot(token=tg_bot_token)
dp = Dispatcher()

# Регистрируем хендлеры
dp.message.register(start_command, CommandStart())  # /start
dp.message.register(help_command, Command("help"))    # /help
dp.message.register(about_command, Command("about"))  # /about
dp.message.register(message_handler) 
dp.callback_query.register(callback_handler)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())