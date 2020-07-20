class IGModel:

    RANGE_ID = 'Iніціативна група!A2'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet

    def get(self):
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
        else:
            print('Name, Major:')
            for row in values:
              print(row)