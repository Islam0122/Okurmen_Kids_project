from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def about_us_inline_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(
            text="Instagram",
            url="https://www.instagram.com/okurmen_kids"
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text="WatsApp",
            url="https://api.whatsapp.com/send/?phone=996709677723&text&type=phone_number&app_absent=0"
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text="WebSite",
            url="http://okurmen.kids.tilda.ws/"
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text="Получить консультацию",
            callback_data="kk"
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text="nazad",
            callback_data="start"
        )
    )
    return keyboard.adjust(2,1,1).as_markup()


def start_inline_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="about us", callback_data="about_us"))
    keyboard.add(InlineKeyboardButton(text="group", callback_data="courses"))
    keyboard.add(InlineKeyboardButton(text="Okurmen_kids", callback_data="Okurmen_kids"))
    return keyboard.adjust(1).as_markup()

def return_main_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(
            text="nazad",
            callback_data="start"
        )
    )
    return keyboard.adjust(2).as_markup()