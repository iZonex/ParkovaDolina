from .model import CSVModel


class IGModel(CSVModel):

    DB_NAME = "ig"

    def __init__(self, service):
        self._service = service
        self._data = self.load_data()

    def load_data(self):
        result = self.read_from_db()
        return " ".join(row[0] for row in result[1:])

    def get(self):
        return self._data