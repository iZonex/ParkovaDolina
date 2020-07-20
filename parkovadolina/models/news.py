class Person:

    def __init__(self, dao, full_name, photo, short_description, link):
        self.dao = dao
        self.full_name = full_name
        self.photo = photo
        self.short_description = short_description
        self.link = link

    def __contains__(self, item):
        return self.full_name.lower() == item.lower()

class PersonsModel:

    RANGE_ID = 'Персони!A2:D'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = []

    def get(self, force=False):
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        self._data = [Person(self, full_name, photo, short_description, link) for full_name, photo, short_description, link in result]
        return self._data

    def get_person_by_full_name(self, full_name):
        for i in self._data:
            if i.full_name == full_name:
                return i