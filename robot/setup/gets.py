#
# Copyright (C) by Kutty-Angel@Github, < https://github.com/Kutty-Angel >.
#
# This file is part of < https://github.com/Kutty-Angel/robot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Kutty-Angel/robot/blob/main/LICENSE >
#
# All rights reserved !!


from typing import Union
from pyrogram.types import Audio, Message, Voice


def get_url(message_1: Message) -> Union[str, None]:
    messages = [message_1]

    if message_1.reply_to_message:
        messages.append(message_1.reply_to_message)

    text = ""
    offset = None
    length = None

    for message in messages:
        if offset:
            break

        if message.entities:
            for entity in message.entities:
                if entity.type == "url":
                    text = message.text or message.caption
                    offset, length = entity.offset, entity.length
                    break

    if offset in (None,):
        return None

    return text[offset : offset + length]


def get_file_name(audio: Union[Audio, Voice]):
    return f'{audio.file_unique_id}.{audio.file_name.split(".")[-1] if not isinstance(audio, Voice) else "ogg"}'
