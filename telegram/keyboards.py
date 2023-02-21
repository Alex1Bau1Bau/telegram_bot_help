from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = [
    [KeyboardButton(text="Опис програми")],
    [KeyboardButton(text="Потрібна допомога")]
]

main_btns = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True
)


kb2 = [
    [KeyboardButton(text="Поділитися ном. телефона", request_contact=True)]
]

share_contact_btn = ReplyKeyboardMarkup(
    keyboard=kb2,
    resize_keyboard=True
)


kb3 = [
    [KeyboardButton(text="Так")],
    [KeyboardButton(text="Ні")]
]

yes_or_no_btns = ReplyKeyboardMarkup(
    keyboard=kb3,
    resize_keyboard=True
)


kb8 = [
    [KeyboardButton(text="Поділитися локацією", request_location=True)]
]

share_location_btn = ReplyKeyboardMarkup(
    keyboard=kb8,
    resize_keyboard=True
)


kb0 = [
    [KeyboardButton(text="Припинити > до Головного меню")]
]

cancel_btn = ReplyKeyboardMarkup(
    keyboard=kb0,
    resize_keyboard=True
)
