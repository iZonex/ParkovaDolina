
from .model import CSVModel


class CheckedGroupModel(CSVModel):

    DB_NAME = "checked_group"

    def __init__(self, service):
        self._service = service
        self._data = self.load_data()

    def load_data(self):
        values = self.read_from_db()
        return " ".join(row[0] for row in values[1:])

    def get(self):
        return self._data
