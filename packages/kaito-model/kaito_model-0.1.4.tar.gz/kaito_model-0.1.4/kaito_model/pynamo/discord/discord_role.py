from pynamodb.attributes import BooleanAttribute
from pynamodb.attributes import MapAttribute
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import UTCDateTimeAttribute

from kaito_model.pynamo.pynamo_base_model import PynamoBaseModel


def get_pynamo_discord_role_model(aws_table_name, aws_region):
    class PynamoDiscordRole(PynamoBaseModel):
        guild_id = UnicodeAttribute(hash_key=True)
        role_id = UnicodeAttribute(range_key=True)
        role_blob = MapAttribute(null=False)
        official_flag = BooleanAttribute(null=False)
        updated_at = UTCDateTimeAttribute(null=True)

        class Meta:
            table_name = aws_table_name
            region = aws_region

        @classmethod
        def contains_official_role(cls, guild_id: str, role_ids: list[str]) -> bool:
            roles = cls.query(guild_id)
            return any(
                [role.official_flag for role in roles if role.role_id in role_ids]
            )

    return PynamoDiscordRole
