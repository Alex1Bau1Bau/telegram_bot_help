from pprint import pprint

from aiogram import Router, F
from aiogram.filters import Text, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from telegram.keyboards import share_location_btn, main_btns, cancel_btn, share_contact_btn, yes_or_no_btns

import csv
from os.path import exists
HEADER_CREATED = False

def save_to_csv(data: dict, path_to_file: str, file_exists: bool):
    with open(path_to_file, 'a', encoding='utf-8') as file:
        fields_name = ['name', 'surname', 'contact', 'ambulan', 'danger', 'lostm', 'details_problem', 'location']
        writer = csv.DictWriter(file, fieldnames=fields_name)

        global HEADER_CREATED
        if not file_exists and not HEADER_CREATED:
            writer.writeheader()
            HEADER_CREATED = True
        writer.writerow(data)

path_to_file = 'data.csv'
file_exists = exists(path_to_file)

class Interview(StatesGroup):
    name = State()
    surname = State()
    contact = State()
    ambulan = State()
    danger = State()
    lostm = State()
    details_problem = State()
    # age = State()
    location = State()

fsm_router = Router()

@fsm_router.message(Text(text=["Опис програми"]))
async def command_interview(message: Message, state: FSMContext) -> None:
    await message.answer(
        "Знайомство з программою. \n"
        "Ця програма дозволяє швидко реагувати на вашу допомогу. Після проходження опитування.\n"
        "Ваші дані обробляються та надходять нашому операторові, який допомагає вам далі з вашим питанням.\n"
        "УВАГА! ЯКЩО ВАМ ДУЖЕ ПОТРІБНА ДОПОМОГА, ви можете пропустити поле вводу, ввівши любу букву, і далі "
        "перейти до швидкого опитування. ",
        reply_markup=cancel_btn,
    )

@fsm_router.message(Text(text=["Потрібна допомога"]))
async def command_interview(message: Message, state: FSMContext) -> None:
    await state.set_state(Interview.name)
    await message.answer(
        "Ваше Ім’я?",
        reply_markup=cancel_btn,
    )

@fsm_router.message(Text(text=["Припинити > до Головного меню"]))
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    # if current_state is None:
    #     return
    print("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=main_btns,
    )

# @fsm_router.message(Interview.name)
# async def set_name(message: Message, state: FSMContext):
#     print('312312')
#     await state.update_data(name=message.text)
#     await state.set_state(Interview.age)
#     await message.answer("Скільки вам років?",
#                          reply_markup=cancel_btn)

@fsm_router.message(Interview.name)
async def set_name(message: Message, state: FSMContext):
    print('312312')
    await state.update_data(name=message.text)
    await state.set_state(Interview.surname)
    await message.answer("Ваша Фамілія?",
                         reply_markup=cancel_btn)

@fsm_router.message(Interview.surname)
async def set_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(Interview.contact)
    await message.answer("Передати номер телефону",
                         reply_markup=share_contact_btn)

@fsm_router.message(Interview.contact)
async def set_surname(message: Message, state: FSMContext):
    contact = message.contact
    await state.update_data(contact=contact.phone_number)
    await state.set_state(Interview.ambulan)
    await message.answer("Вам потрібна швидка допомога?",
                         reply_markup=yes_or_no_btns)

@fsm_router.message(Interview.ambulan)
async def set_surname(message: Message, state: FSMContext):
    await state.update_data(ambulan=message.text)
    await state.set_state(Interview.danger)
    await message.answer("Вам щось загрожує?",
                         reply_markup=yes_or_no_btns)

@fsm_router.message(Interview.danger)
async def set_surname(message: Message, state: FSMContext):
    await state.update_data(danger=message.text)
    await state.set_state(Interview.lostm)
    await message.answer("Ви загубилися?",
                         reply_markup=yes_or_no_btns)

@fsm_router.message(Interview.lostm)
async def set_lostm(message: Message, state: FSMContext):
    await state.update_data(lostm=message.text)
    await state.set_state(Interview.details_problem)
    await message.answer("Опишіть подробиці проблеми.",
                         reply_markup=cancel_btn)

@fsm_router.message(Interview.details_problem)
async def set_lostm(message: Message, state: FSMContext):
    await state.update_data(details_problem=message.text)
    await state.set_state(Interview.location)
    await message.answer("Передати локацію",
                         reply_markup=share_location_btn)

@fsm_router.message(Interview.location)
async def set_location(message: Message, state: FSMContext):
    location = message.location
    location2 = 'log = ' + str(location.longitude) + ' lat = ' + str(location.latitude)
    await state.update_data(location=location2)
    data_about_user = await state.get_data()
    save_to_csv(data_about_user, path_to_file, file_exists)
    await state.clear()
    # show data
    pprint(data_about_user)
    await message.answer("Ми вас почули, чекайте на допомогу!",
                         reply_markup=main_btns)
