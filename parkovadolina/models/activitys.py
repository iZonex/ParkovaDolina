class Activity:

    def __init__(self, dao, title, actions_description, source_link, due_date, status):
        self.dao = dao
        self.title = title
        self.actions_description = actions_description
        self.source_link = source_link
        self.due_date = due_date
        self.status = status


class ActivitysModel:

    RANGE_ID = 'Активності!A2:E'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = []

    def get(self, force=False):
        result = self._service.values().get(spreadsheetId=self._sheet,
                                            range=self.RANGE_ID).execute().get('values', [])

        self._data = [Activity(self, title, actions_description, source_link, due_date, status)
                      for title, actions_description, source_link, due_date, status in result]
        return self._data

    def get_activity_by_title(self, title):
        for i in self._data:
            if i.title == title:
                return i
