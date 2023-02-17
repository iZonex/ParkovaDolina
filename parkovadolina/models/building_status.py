import time
from collections import Counter
from datetime import datetime
import uuid

from parkovadolina.models.building_constants import (BUILDING_NUMBERS,
                                                     BUILDING_NUMBERS_REVERSED,
                                                     STATUS_MAP_REVERSED)

from .model import CSVModel


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


class BuildingStatusModel(CSVModel):

    DB_NAME = 'building_status'

    def __init__(self, service):
        self._service = service
        self._ttl = time.time()
        self._data = self.load_data()
        self._ttl_building_status = time.time()
        self._building_status_results = {i: "1" for i in BUILDING_NUMBERS.keys()}

    def load_data(self):
        data = {}
        result = self.read_from_db()
        for uid, building_name, status, date, user_id in result[1:]:
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
        start_date = datetime.now().replace(day=1)
        for building_id in self._data.keys():
            result_status = Counter([obj.status for obj in self._data[building_id] if obj.date >= start_date])
            try:
                self._building_status_results[building_id] = str(result_status.most_common(1)[0][0])
            except IndexError:
                self._building_status_results[building_id] = "1"
        return self._building_status_results

    def create(self, building_name,	status,	user_id):
        building_id = BUILDING_NUMBERS_REVERSED[building_name]
        status = STATUS_MAP_REVERSED[str(status)]
        date = int(time.time())
        uid = str(uuid.uuid4())
        values = [uid, building_id, status, date, user_id]
        if not building_id in self._data:
            self._data[building_id] = []
        self._data[building_id].append(BuildingStatus(
            self, uid, building_id, status, int(date), user_id))
        self.write_to_db(values)
