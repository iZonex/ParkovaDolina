import uuid
from parkovadolina.core.constants import MAIN_MENU
from .model import CSVModel
class User:

    def __init__(self, dao, uid, user_id, agreement):
        self.dao = dao
        self.uid = uid
        self.user_id = user_id
        self.agreement = agreement

    def save(self):
        self.dao.update(self.uid, self.user_id, self.agreement)

    def __contains__(self, item):
        return self.user_id == item
        
class UsersModel(CSVModel):

    DB_NAME = "users"

    def __init__(self, service):
        self._service = service
        self._data = self.load_data()

    def load_data(self):
        result = self.read_from_db()
        return {int(data[1]): User(self, data[0], int(data[1]), bool(data[2])) for data in result[1:] if data}

    def get(self):
        return self._data

    def get_by_user_id(self, user_id):
        return self._data.get(user_id, None)
        
    def create(self, user_id):
        if not self.get_by_user_id(user_id):
            uid = str(uuid.uuid4())
            values = [uid, user_id, 1]
            self._data[user_id] = User(self, uid, int(user_id), bool(1))
            self.write_to_db(values)
            
