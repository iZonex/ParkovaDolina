class IGModel:

    RANGE_ID = 'Iніціативна група!A2'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = self.load_data()

    def load_data(self):
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute()
        values = result.get('values', [])
        return [" ".join(row) for row in values][0]

    def get(self):
        return self._data