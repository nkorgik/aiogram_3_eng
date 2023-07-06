import asyncio

from aiogram import types, Dispatcher, Bot
from aiogram.filters import Command

from token_api import TOKEN


bot = Bot(token=TOKEN)
dispatcher = Dispatcher()


@dispatcher.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    """Handle start command"""
    
    reply_text = f'Hello, {msg.from_user.first_name}! ❤️‍🩹'
    
    await msg.answer(
        text=reply_text
    )
    
    await msg.reply(
        text=reply_text
    )
    

@dispatcher.message(Command('help'))
async def cmd_help(msg: types.Message) -> None:
    """Handle help command"""
    
    reply_text = f'Help command.'
    
    await msg.answer(
        text=reply_text
    )
    
    await msg.reply(
        text=reply_text
    )


async def main() -> None:
    """Entry point"""

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
