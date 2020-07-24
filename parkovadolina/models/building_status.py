import datetime

class BuildingStatus:

    BUILDING_NUMBERS = {
        "1": "Будинок №1 Секція №1-3",
        "2": "Будинок №1 Секція №4-6",
        "3": "Будинок №1 Секція №7-9",
        "4": "Будинок №2 Секція №1",
        "5": "Будинок №2 Секція №2",
        "6": "Будинок №2 Секція №3",
        "7": "Будинок №2 Секція №4",
    }

    def __init__(self, dao, title_id):
        self.dao = dao
        self.title_id = title_id
        self.states = {}

    @property
    def title(self):
        return self.BUILDING_NUMBERS.get(self.title_id)

    def get_expected_state(self):
        return self.states.get([datetime.datetime.now().replace(day=1).date()])

class BuildingPlanModel:

    RANGE_ID = 'Прогрес будівництва!A1:V'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = self._load_data()

    def _load_data(self):
        data = {}
        rows = self._service.values().get(spreadsheetId=self._sheet,
                                            range=self.RANGE_ID).execute().get('values', [])

        header = [datetime.datetime.strptime(i, '%d.%m.%Y').date() for i in rows[0][1:]]

        for row in rows[1:]:
            states = {}
            for number, states_raw_string in enumerate(row[1:]):
                states[header[number]] = states_raw_string.split(",")
            data[row[0]] = BuildingPlan(self, row[0], states)

        return data

    def get(self):
        return self._data

    def get_by_building(self, title):
        return self._data[title]