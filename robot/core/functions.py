#
# Copyright (C) by Kutty-Angel@Github, < https://github.com/Kutty-Angel >.
#
# This file is part of < https://github.com/Kutty-Angel/robot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Kutty-Angel/robot/blob/main/LICENSE >
#
# All rights reserved !!


from typing import Dict, List, Union

from robot.core import db


restart_stagedb = db.restart_stage


async def start_restart_stage(chat_id: int, message_id: int):
    await restart_stagedb.update_one(
        {"something": "something"},
        {
            "$set": {
                "chat_id": chat_id,
                "message_id": message_id,
            }
        },
        upsert=True,
    )


async def clean_restart_stage() -> dict:
    data = await restart_stagedb.find_one({"something": "something"})
    if not data:
        return {}
    await restart_stagedb.delete_one({"something": "something"})
    return {"chat_id": data["chat_id"], "message_id": data["message_id"]}
