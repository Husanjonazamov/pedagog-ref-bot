# start.py
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio.tasks import create_task

from loader import dp, bot
from utils import texts, buttons
from services.services import botUser

async def _task(message: Message, state: FSMContext):
    """
    Botning asosiy /start handleri
    """
    lang = message.from_user.language_code
    text = texts.START[lang]
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    result = botUser(tg_id=user_id, first_name=first_name)

    if result.get("exists"):
        print(f"User already exists: {user_id}")
    else:
        print(f"New user created: {result}")

    buttons.send_webapp_button(lang=lang, user_id=user_id, text=text)


@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))
