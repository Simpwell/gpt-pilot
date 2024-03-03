import json
from peewee import TextField


class JSONField(TextField):
    def python_value(self, value):
        if value is not None:
            return json.loads(value)
        return value

    def db_value(self, value):
        if value is not None:
            return json.dumps(value,ensure_ascii=False)
        return value
