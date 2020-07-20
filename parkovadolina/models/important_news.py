class ImportantNews:

    def __init__(self, dao, uid=None, username=None, text=None, date=None):
        self.dao = dao
        self.uid = uid
        self.username = username
        self.text = text
        self.date = date

    def __contains__(self, uid):
        return self.uid == uid
        
class ImportantNewsModel:

    RANGE_ID = 'Важливі новини!A2:D'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = []

    def get(self, force=False):
        if self._data and not force:
            return self._data
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        self._data = [ImportantNews(self, uid, username, text, date) for uid, username, text, date in result][::-1]
        return self._data
        
    def create(self, username, text, date):
        next_row = len(self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])) + 2
        values = [[next_row, username, text, date]]
        body = {'values': values, 'majorDimension' : 'ROWS'}
        self._service.values().update(spreadsheetId=self._sheet, range=f'Важливі новини!A{next_row}:D', valueInputOption='RAW', body=body).execute()
        self.get(force=True)
