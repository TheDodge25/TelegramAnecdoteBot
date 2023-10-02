import asyncio
import logging
import sys
from os import getenv, environ

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

from page_parser import requestAndProcess


load_dotenv()
TOKEN = getenv("TELEGRAM_TOKEN")  # Telegram bot token, loaded from .env file


# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
rt = Router()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


# if command is "/anecdote" - send an anecdote, pretty simple
@dp.message(Command('anecdote'))
async def send_anecdote(message: types.Message) -> None:
    anecdote = await requestAndProcess()
    await message.answer(anecdote)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed
    # to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # one line before replaced "TOKEN" variable with the token itself
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
