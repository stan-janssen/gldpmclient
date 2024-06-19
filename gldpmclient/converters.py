import re
from datetime import datetime, timezone

from xsdata.formats.converter import Converter, converter


class DateTimeConverter(Converter):
    DT_FORMAT = "%Y-%m-%dT%H:%M%z"

    def deserialize(self, value: str, **kwargs) -> datetime:
        return datetime.strptime(value, kwargs.get('format') or self.DT_FORMAT)

    def serialize(self, value: datetime, **kwargs) -> str:
        return re.sub(r"\+00:?00", "Z", value.astimezone(timezone.utc).strftime(kwargs.get('format') or self.DT_FORMAT))


converter.register_converter(datetime, DateTimeConverter())
