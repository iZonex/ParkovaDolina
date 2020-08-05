
import uuid

class Notifications:

    def __init__(self, dao, uid=None, user_id=None, text=None, time=None):
        self.dao = dao
        self.uid = uid
        self.user_id = user_id
        self.text = text
        self.time = time


class  NotificationsModel:

    def __init__(self):
        self._data = {}
        self._users_notification = {}

    def get_by_user_remainders(self, user_id):
        return  self._users_notification.get(user_id, [])

    def get_by_uid(self, uid):
        return self._data.get(uid, None)

    def add_user_remainder(self, user_id, text, time):
        uid = str(uuid.uuid4())
        self._data[uid] = Notifications(self, uid, text, time)
        if not self._users_notification.get(user_id, None):
            self._users_notification[user_id] = []
        self._users_notification[user_id].append(uid)

    def remove_user_remainder(self, uid):
        self._users_notification[self._data.pop(uid).user_id].remove(uid)