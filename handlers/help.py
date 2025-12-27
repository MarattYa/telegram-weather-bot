from aiogram import types 
from aiogram.filters import Command 

async def help_command(message: types.Message): 
    await message.answer( "Просто напиши название города, и я пришлю погоду!" )