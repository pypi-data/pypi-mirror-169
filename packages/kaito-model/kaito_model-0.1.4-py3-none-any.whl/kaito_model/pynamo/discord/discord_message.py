from pynamodb.attributes import MapAttribute
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import UTCDateTimeAttribute

from kaito_model.pynamo.pynamo_base_model import PynamoBaseModel


def get_pynamo_discord_message_model(aws_table_name, aws_region):
    class PynamoDiscordMessage(PynamoBaseModel):

        channel_id = UnicodeAttribute(hash_key=True)
        timestamp = UTCDateTimeAttribute(range_key=True)
        message = MapAttribute(null=False)
        updated_at = UTCDateTimeAttribute(null=True)

        class Meta:
            table_name = aws_table_name
            region = aws_region

        def get_server_id(self) -> str:
            return self.message["server_id"]

        def get_author(self) -> str:
            return self.message["author"]

        def get_author_role_ids(self) -> list[str]:
            return [role["id"] for role in self.message["author"]["roles"]]

    return PynamoDiscordMessage
