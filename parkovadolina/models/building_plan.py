import datetime
from dateutil.relativedelta import relativedelta

class BuildingPlan:


    BUILDING_NUMBERS = {
        "1": "Будинок №1 Секція №1-3",
        "2": "Будинок №1 Секція №4-6",
        "3": "Будинок №1 Секція №7-9",
        "4": "Будинок №2 Секція №1",
        "5": "Будинок №2 Секція №2",
        "6": "Будинок №2 Секція №3",
        "7": "Будинок №2 Секція №4",
    }

    def __init__(self, dao, title_id, states):
        self.dao = dao
        self.title_id = title_id
        self.states = states

    def get_expected_state(self):
        start_of_month = datetime.datetime.now().replace(day=1).date()
        return self.states.get(start_of_month)

    @property
    def title(self):
        return self.BUILDING_NUMBERS.get(self.title_id, "None")

    def get_date(self):
        return datetime.datetime.now().replace(day=1).strftime("%d.%m.%Y")


class BuildingPlanModel:

    RANGE_ID = 'Прогрес будівництва!A1:V'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._map_dates = self._date_map(datetime.datetime(month=7, day=1, year=2020))
        self._data = self.load_data()
       
    def _date_map(self, start_date):
        return {str(i):(start_date + relativedelta(months=i)).date() for i in range(30)}
        
    def load_data(self):
        data = {}
        rows = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        header = [self._map_dates[i] for i in rows[0][1:]]

        for row in rows[1:]:
            states = {}
            for number, states_raw_string in enumerate(row[1:]):
                states[header[number]] = states_raw_string.split(",")
            obj = BuildingPlan(self, row[0], states)
            data[obj.title] = obj
        return data

    def get(self):
        return self._data

    def get_by_building_title(self, title):
        return self._data[title]