#
# Copyright (C) by Kutty-Angel@Github, < https://github.com/Kutty-Angel >.
#
# This file is part of < https://github.com/Kutty-Angel/robot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Kutty-Angel/robot/blob/main/LICENSE >
#
# All rights reserved !!


from typing import Callable
from pyrogram import Client
from pyrogram.types import Message

from robot.config import SUDO_USERS


def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return decorator
