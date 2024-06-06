import asyncio
from modules import module_commands


async def handle_message(text, chat_id, session, replied_text=""):
    parsed = str(text).split(' ')
    if parsed[0].lower() in module_commands.commands:
        task = asyncio.create_task(module_commands.commands[parsed[0].lower()](text, chat_id, session, replied_text))
        await task
    elif text[:3].lower() == 'ква':
        task = asyncio.create_task(module_commands.commands[text[:3].lower()](text, chat_id, session, replied_text))
        await task


async def handle_post(post_id, session):
    task = asyncio.create_task(module_commands.func_repost(post_id, session))
    await task
