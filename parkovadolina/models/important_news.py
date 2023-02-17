import time

from .model import CSVModel
class ImportantNews:

    def __init__(self, dao, uid=None, username=None, text=None, date=None):
        self.dao = dao
        self.uid = uid
        self.username = username
        self.text = text
        self.date = date

    def __contains__(self, uid):
        return self.uid == uid
        
class ImportantNewsModel(CSVModel):

    DB_NAME = "important_news"

    def __init__(self, service):
        self._service = service
        self._data = self.load_data()

    def load_data(self):
        result = self.read_from_db()
        return [ImportantNews(self, uid, username, text, date) for uid, username, text, date in result[1:]][::-1]
    
    def get(self):
        return self._data
        
    def create(self, username, text, date):
        next_row = len(self._data) + 2
        values = [next_row, username, text, date]
        self.write_to_db(values)
        self.__data.insert(0, ImportantNews(next_row, username, text, date))
