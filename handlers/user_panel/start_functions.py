from aiogram import  F, types,Router
from aiogram.filters import Command

start_functions_router = Router()

welcome_message = (
    """
    kow keliniz okurmen kidske
    """
)
@start_functions_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer_photo(photo=types.FSInputFile("media/logo.jpg"), caption=welcome_message)