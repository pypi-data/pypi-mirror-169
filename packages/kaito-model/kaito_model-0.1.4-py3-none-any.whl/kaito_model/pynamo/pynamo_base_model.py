from datetime import datetime
from uuid import UUID

from pynamodb.attributes import MapAttribute
from pynamodb.models import Model


class PynamoBaseModel(Model):
    """A base class for DynamoDb models."""

    def to_dict(self):
        """Converts a pynamodb object to a dictionary."""
        rval = {}

        for key in self.attribute_values:
            value = self.__getattribute__(key)
            # Convert MapAttribute to dictionary
            if isinstance(value, MapAttribute):
                value = value.as_dict()
            elif isinstance(value, UUID):
                value = str(value)
            elif isinstance(value, datetime):
                value = value.isoformat()
            rval[key] = value

        return rval
