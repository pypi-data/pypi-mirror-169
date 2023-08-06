import json
from datetime import datetime

from kaito_model.discord.discord_base import DiscordBaseObject
from kaito_model.mapper.object_mapper import ObjectMapper
from kaito_model.pynamo.discord.discord_role import get_pynamo_discord_role_model
from kaito_model.pynamo.pynamo_base_model import PynamoBaseModel


class Role(DiscordBaseObject):
    class_identifier = "discord_role"

    def __init__(
        self, guild_id: str, role_id: str, role_blob: dict, official_flag: bool = None
    ) -> None:
        self.guild_id = guild_id
        self.role_id = role_id
        self.role_blob = role_blob
        self.official_flag = official_flag
        self.updated_at = datetime.utcnow()

    @classmethod
    def from_json_string(cls, json_str: str):
        role = json.loads(json_str)
        return cls(guild_id=role["guild_id"], role_id=role["role_id"], role_blob=role)
