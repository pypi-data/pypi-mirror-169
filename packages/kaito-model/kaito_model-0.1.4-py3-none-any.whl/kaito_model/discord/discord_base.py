import json

from kaito_model.mapper.object_mapper import ObjectMapper
from kaito_model.pynamo.discord.discord_role import get_pynamo_discord_role_model
from kaito_model.pynamo.pynamo_base_model import PynamoBaseModel


class DiscordBaseObject(object):
    """A base class for Discord models."""

    mapper = ObjectMapper()
    class_identifier = None

    # Always override to_json() method to return a JSON string, some data types (datetime, dict, etc) are not JSON serializable
    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=str)

    @classmethod
    def setup_mapper(cls, table_name, region) -> None:
        if cls.class_identifier == "discord_role":
            DiscordRoleModel = get_pynamo_discord_role_model(
                table_name_arg=table_name, aws_region=region
            )
        else:
            raise Exception("Class identifier not found")
        if not cls.mapper.mappings:
            cls.mapper.create_map(cls, DiscordRoleModel)

    def to_pynamo_model(self, allow_unmapped=True) -> PynamoBaseModel:
        """_summary_: Convert a DiscordBaseObject to a PynamoBaseModel.

        Args:
            allow_unmapped (bool, optional): Whether to map all fields mandatorily.
            Usually DiscordBaseObject adopt from discord which has a lot of fields,
            but PynamoBaseModel only has a few fields.

            Defaults to True.

        Raises:
            Exception: _description_

        Returns:
            PynamoBaseModel: A PynamoBaseModel object
        """
        if not self.mapper.mappings:
            raise Exception(
                "ObjectMapper is not initialized. Please call setup_mapper() first."
            )
        return self.mapper.map(self, allow_unmapped=allow_unmapped)
