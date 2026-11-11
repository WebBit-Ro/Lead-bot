import asyncio
import logging
import re
from html import escape

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from config import ADMIN_CHAT_ID, BOT_TOKEN

router = Router()

SERVICE_OPTIONS = {
    "website": "Website",
    "telegram_bot": "Telegram Bot",
    "automation": "Automation",
}

BUDGET_OPTIONS = {
    "100_300": "$100–$300",
    "300_700": "$300–$700",
    "700_plus": "$700+",
}

USERNAME_PATTERN = re.compile(r"^@?[A-Za-z][A-Za-z0-9_]{4,31}$")
PHONE_PATTERN = re.compile(r"^\+?[\d\s().-]{7,24}$")


class LeadForm(StatesGroup):
    service = State()
    budget = State()
    contact = State()


def service_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Website", callback_data="service:website")],
            [InlineKeyboardButton(text="Telegram Bot", callback_data="service:telegram_bot")],
            [InlineKeyboardButton(text="Automation", callback_data="service:automation")],
        ]
    )


def budget_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="$100–$300", callback_data="budget:100_300")],
            [InlineKeyboardButton(text="$300–$700", callback_data="budget:300_700")],
            [InlineKeyboardButton(text="$700+", callback_data="budget:700_plus")],
        ]
    )


def contact_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Share phone number", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


@router.message(CommandStart())
async def start_quiz(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(LeadForm.service)
    await message.answer(
        "Hi! Let's find the right solution for your project.\n\nWhat service are you interested in?",
        reply_markup=service_keyboard(),
    )


@router.callback_query(LeadForm.service, F.data.startswith("service:"))
async def select_service(callback: CallbackQuery, state: FSMContext):
    service_key = callback.data.removeprefix("service:")
    if service_key not in SERVICE_OPTIONS:
        await callback.answer("Invalid option.", show_alert=True)
        return

    await state.update_data(service=SERVICE_OPTIONS[service_key])
    await state.set_state(LeadForm.budget)
    await callback.answer()

    if callback.message:
        await callback.message.edit_text(
            "What is your approximate budget?",
            reply_markup=budget_keyboard(),
        )


@router.callback_query(LeadForm.budget, F.data.startswith("budget:"))
async def select_budget(callback: CallbackQuery, state: FSMContext):
    budget_key = callback.data.removeprefix("budget:")
    if budget_key not in BUDGET_OPTIONS:
        await callback.answer("Invalid option.", show_alert=True)
        return

    await state.update_data(budget=BUDGET_OPTIONS[budget_key])
    await state.set_state(LeadForm.contact)
    await callback.answer()

    if callback.message:
        await callback.message.edit_text("Great. One last step: share your contact details.")
        await callback.message.answer(
            "Tap the button to share your phone number, or type your Telegram username (for example, @username).",
            reply_markup=contact_keyboard(),
        )


async def submit_lead(message: Message, state: FSMContext, contact_value: str):
    if message.from_user is None:
        return

    lead_data = await state.get_data()
    user = message.from_user
    telegram_contact = (
        f"@{escape(user.username)}"
        if user.username
        else f'<a href="tg://user?id={user.id}">Open Telegram profile</a>'
    )
    summary = (
        "<b>New lead</b>\n\n"
        f"<b>Service:</b> {escape(lead_data['service'])}\n"
        f"<b>Budget:</b> {escape(lead_data['budget'])}\n"
        f"<b>Contact:</b> {escape(contact_value)}\n"
        f"<b>Name:</b> {escape(user.full_name)}\n"
        f"<b>Telegram:</b> {telegram_contact}"
    )

    try:
        await message.bot.send_message(chat_id=ADMIN_CHAT_ID, text=summary)
    except TelegramAPIError:
        logging.exception("Could not deliver a lead to the admin chat")
        await message.answer(
            "Your request could not be submitted right now. Please try sharing your contact again.",
            reply_markup=contact_keyboard(),
        )
        return

    await state.clear()
    await message.answer(
        "Thank you! Your request has been sent. We'll be in touch soon.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(LeadForm.contact, F.contact)
async def receive_phone(message: Message, state: FSMContext):
    if message.contact is None:
        return

    if message.from_user is None or (
        message.contact.user_id is not None
        and message.contact.user_id != message.from_user.id
    ):
        await message.answer("Please share your own phone number using the button below.")
        return

    await submit_lead(message, state, message.contact.phone_number)


@router.message(LeadForm.contact, F.text)
async def receive_text_contact(message: Message, state: FSMContext):
    value = message.text.strip()

    if USERNAME_PATTERN.fullmatch(value):
        contact_value = value if value.startswith("@") else f"@{value}"
    elif PHONE_PATTERN.fullmatch(value) and 7 <= len(re.sub(r"\D", "", value)) <= 15:
        contact_value = value
    else:
        await message.answer(
            "Please enter a valid phone number or Telegram username, such as @username."
        )
        return

    await submit_lead(message, state, contact_value)


async def main():
    logging.basicConfig(level=logging.INFO)

    async with Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    ) as bot:
        dispatcher = Dispatcher(storage=MemoryStorage())
        dispatcher.include_router(router)
        await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
