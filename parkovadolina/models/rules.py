class RulesModel:

    RANGE_ID = 'Правила!A2:D'

    def __init__(self, service, sheet, cache_ttl):
        self._service = service
        self._sheet = sheet
        self._cache_ttl = cache_ttl
        self._data = self.load_data()

    def load_data(self):
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute()
        values = result.get('values', [])
        return [". ".join(row) for row in values]

    def get(self):
        return self._data
