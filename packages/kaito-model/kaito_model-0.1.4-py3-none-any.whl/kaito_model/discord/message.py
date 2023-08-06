import json
from datetime import datetime

import dateutil.parser

from kaito_model.mapper.object_mapper import ObjectMapper
from kaito_model.pynamo.discord.discord_message import get_pynamo_discord_message_model
from kaito_model.pynamo.pynamo_base_model import PynamoBaseModel


class Message(object):
    class_identifier = "discord_message"

    def __init__(self, channel_id: str, timestamp: str, message: dict) -> None:
        self.channel_id = channel_id
        self.timestamp = datetime.fromisoformat(
            dateutil.parser.isoparse(timestamp).isoformat(timespec="milliseconds")
        )
        self.message = message
        # self.author = author
        self.updated_at = datetime.utcnow()

    @classmethod
    def from_json_string(cls, json_str: str):
        msg = json.loads(json_str)
        return cls(
            channel_id=msg["channel_id"], timestamp=msg["timestamp"], message=msg
        )
