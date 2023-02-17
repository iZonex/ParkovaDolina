
from .model import CSVModel


class RulesModel(CSVModel):

    DB_NAME = "rules"

    def __init__(self, service):
        self._service = service
        self._data = self.load_data()

    def load_data(self):
        result = self.read_from_db()[1:]
        return "\n".join(". ".join(row) for row in result)

    def get(self):
        return self._data
