class User:

    def __init__(self, dao, uid, user_id, agreement):
        self.dao = dao
        self.uid = uid
        self.user_id = user_id
        self.agreement = agreement

    def save(self):
        self.dao.update(self.uid, self.user_id, self.agreement)

    def __contains__(self, item):
        return self.user_id == item
        
class UsersModel:

    RANGE_ID = 'Користувачі!A2:C'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = []

    def get(self, force=False):
        if self._data and not force:
            return self._data
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        self._data = [(User(self, data[0], int(data[1]), bool(data[2]))) for data in result if data]
        return self._data

    def get_by_user_id(self, user_id):
        if not self._data:
            self.get()
        for i in self._data:
            if i.user_id == user_id:
                return i
        return None
        
    def create(self, user_id):
        next_row = len(self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])) + 2
        values = [[next_row, user_id, 1]]
        body = {'values': values, 'majorDimension' : 'ROWS'}
        self._service.values().update(spreadsheetId=self._sheet, range=f'Користувачі!A{next_row}:C', valueInputOption='RAW', body=body).execute()
        self.get(force=True)
