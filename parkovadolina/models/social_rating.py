from core.constants import MAIN_MENU


# TODO Is still in progress
class UserSocialRaiting:

    def __init__(self, dao, uid, user_id, agreement):
        self.dao = dao
        self.uid = uid
        self.user_id = user_id
        self.agreement = agreement

    def save(self):
        self.dao.update(self.uid, self.user_id, self.agreement)

    def __contains__(self, item):
        return self.user_id == item
        
class UserSocialRaitingModel:

    RANGE_ID = 'Користувачі!A2:C'

    def __init__(self, service, sheet, cache_ttl):
        self._service = service
        self._sheet = sheet
        self._cache_ttl = cache_ttl
        self._data = self.load_data()

    def load_data(self):
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        return {int(data[1]): User(self, data[0], int(data[1]), bool(data[2])) for data in result if data}

    def get(self):
        return self._data

    def get_by_user_id(self, user_id):
        return self._data.get(user_id, None)
        
    def create(self, user_id):
        if not self.get_by_user_id(user_id):
            next_row = len(self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])) + 2
            values = [[next_row, user_id, 1]]
            body = {'values': values, 'majorDimension' : 'ROWS'}
            self._data[user_id] = User(self, next_row, int(user_id), bool(1))
            self._service.values().update(spreadsheetId=self._sheet, range=f'Користувачі!A{next_row}:C', valueInputOption='RAW', body=body).execute()
            