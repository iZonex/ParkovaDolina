from core.constants import EXIT

class Session:

    def __init__(self, dao, user_id):
        self.dao = dao
        self.user_id = user_id
        self._context = []

    def get_index(self, text):
        for n, i in enumerate(self._context):
            if text == i[1]:
                return n
        return None

    def register_context(self, route, text):
        cut_index = self.get_index(text)
        if text == EXIT or text == "Головне меню":
            self._context = []
        elif cut_index != None:
            self._context = self._context[:cut_index+1]
        else:
            self._context.append((route, text))

    def get_context(self):
        # print(f"User {self.user_id} Context: {' >>> '.join(self._context)}")
        return self._context
        
class SessionModel:

    def __init__(self):
        self._data = {}

    def get_by_user_id(self, user_id):
        return self._data.get(user_id, None)
        
    def create(self, user_id):
        if not self.get_by_user_id(user_id):
            self._data[user_id] = Session(self, int(user_id))