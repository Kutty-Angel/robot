#
# Copyright (C) by Kutty-Angel@Github, < https://github.com/Kutty-Angel >.
#
# This file is part of < https://github.com/Kutty-Angel/robot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Kutty-Angel/robot/blob/main/LICENSE >
#
# All rights reserved !!


from typing import List, Union
from pyrogram import filters

from robot.config import CMD_MUSIC, SUDO_USERS


other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded

other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, CMD_MUSIC)
