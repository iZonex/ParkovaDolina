from parkovadolina.core.constants import EXIT, MAIN_MENU

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

    def register_context(self, route=None, text=None):
        cut_index = self.get_index(text)
        if text == EXIT or text == MAIN_MENU:
            self._context = []
        elif text == "↩️Назад":
            self._context = self._context[:-1]
        elif cut_index != None:
            self._context = self._context[:cut_index+1]
        elif route != None:
            self._context.append((route, text))

    def get_context(self):
        return self._context
        
class SessionModel:

    def __init__(self):
        self._data = {}

    def get(self, user_id):
        return self._data[user_id]
        
    def create(self, user_id):
        if not self._data.get(user_id):
            self._data[user_id] = Session(self, user_id)