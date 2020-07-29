import time
from datetime import datetime
from parkovadolina.core.constants import EXIT

STATUS_MAP = {
    "1": "✅Все добре",
    "2": "❌Зупинено",
    "3": "❗️Помічені проблеми"
}

BUILDING_NUMBERS = {
    "1": "Будинок №1 Секція №1-3",
    "2": "Будинок №1 Секція №4-6",
    "3": "Будинок №1 Секція №7-9",
    "4": "Будинок №2 Секція №1",
    "5": "Будинок №2 Секція №2",
    "6": "Будинок №2 Секція №3",
    "7": "Будинок №2 Секція №4",
}

BUILDING_NUMBERS_REVERSED = {v:k for k,v in BUILDING_NUMBERS.items()}

STATUS_MAP_REVERSED = {v:k for k,v in STATUS_MAP.items()}
class BuildingStatus:

    def __init__(self, dao, uid, building_id, status, date, user_id):
        self.dao = dao
        self.uid = uid
        self.building_id = building_id
        self.status = status
        self._date = int(date)
        self.user_id = user_id
    
    @property
    def name(self):
        return BUILDING_NUMBERS[self.building_id]

    @property
    def date(self):
        return datetime.fromtimestamp(self._date)
        
class BuildingStatusModel:

    RANGE_ID = 'Аудит Будівництва!A2:E'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = self.load_data()

    def load_data(self):
        data = {}
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        for uid, building_name, status, date, user_id in result:
            if not building_name in data:
                data[building_name] = []
            data[building_name].append(BuildingStatus(self, uid, building_name, status, int(date), user_id))
        return data

    def get(self):
        return self._data

    def get_by_building(self, name):
        return self._data[name]
        
    def create(self, building_name,	status,	user_id):
        building_id = BUILDING_NUMBERS_REVERSED[building_name]
        status = STATUS_MAP_REVERSED[str(status)]
        date = int(time.time())
        uid = len(self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])) + 2
        values = [[uid, building_id, status, date, user_id]]
        body = {'values': values, 'majorDimension' : 'ROWS'}
        if not building_id in self._data: 
            self._data[building_id] = []
        self._data[building_id].append(BuildingStatus(self, uid, building_id, status, int(date), user_id))
        self._service.values().update(spreadsheetId=self._sheet, range=f'Аудит Будівництва!A{uid}:E', valueInputOption='RAW', body=body).execute()
            
