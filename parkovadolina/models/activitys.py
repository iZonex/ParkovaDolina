from .model import CSVModel


class Activity:

    def __init__(self, dao, title, actions_description, source_link, due_date, status):
        self.dao = dao
        self.title = title
        self.actions_description = actions_description
        self.source_link = source_link
        self.due_date = due_date
        self.status = status


class ActivitysModel(CSVModel):

    DB_NAME = "activitys"

    def __init__(self, service):
        self._service = service
        self._data = self.load_data()

    def load_data(self):
        result = self.read_from_db()[1:]

        self._data = [Activity(self, title, actions_description, source_link, due_date, status)
                      for title, actions_description, source_link, due_date, status in result]
        return self._data

    def get(self, force=False):
        return self._data

    def get_activity_by_title(self, title):
        for i in self._data:
            if i.title == title:
                return i
