from collections import Counter
from parkovadolina.models.building_constants import BUILDING_NUMBERS, BUILDING_NUMBERS_REVERSED, STATUS_MAP_REVERSED
import time
from datetime import datetime


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
        self._ttl = time.time()
        self.__data = {}
        self._ttl_building_status = time.time()
        self._building_status_results = {i: "1" for i in BUILDING_NUMBERS.keys()}
        
    @property
    def _data(self):
        if time.time() >= self._ttl:
            self._ttl = time.time() + 86400 
            self.__data = self.load_data()
        return self.__data

    def load_data(self):
        data = {}
        result = self._service.values().get(spreadsheetId=self._sheet,
                                            range=self.RANGE_ID).execute().get('values', [])
        for uid, building_name, status, date, user_id in result:
            if not building_name in data:
                data[building_name] = []
            data[building_name].append(BuildingStatus(
                self, uid, building_name, status, int(date), user_id))
        return data

    def get(self):
        return self._data

    def get_date(self):
        return datetime.now().strftime("%d.%m.%Y")

    def get_by_building(self, name):
        return self._data[name]

    def get_building_status(self):
        if self._ttl_building_status <= time.time():
            start_date = datetime.now().replace(day=1)
            for building_id in self._data.keys():
                result_status = Counter([obj.status for obj in self._data[building_id] if obj.date >= start_date])
                self._building_status_results[building_id] = str(result_status.most_common(1)[0][0])
            self._ttl_building_status = time.time() + 86400
        return self._building_status_results

    def create(self, building_name,	status,	user_id):
        building_id = BUILDING_NUMBERS_REVERSED[building_name]
        status = STATUS_MAP_REVERSED[str(status)]
        date = int(time.time())
        uid = len(self._service.values().get(spreadsheetId=self._sheet,
                                             range=self.RANGE_ID).execute().get('values', [])) + 2
        values = [[uid, building_id, status, date, user_id]]
        body = {'values': values, 'majorDimension': 'ROWS'}
        if not building_id in self._data:
            self._data[building_id] = []
        self._data[building_id].append(BuildingStatus(
            self, uid, building_id, status, int(date), user_id))
        self._service.values().update(spreadsheetId=self._sheet,
                                      range=f'Аудит Будівництва!A{uid}:E', valueInputOption='RAW', body=body).execute()
