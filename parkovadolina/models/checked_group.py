class CheckedGroupModel:

    RANGE_ID = 'Група підтверджених інвесторів!A2'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = None

    def get(self):
        if not self._data:
            result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute()
            values = result.get('values', [])
            self._data = [" ".join(row) for row in values]
        return self._data
