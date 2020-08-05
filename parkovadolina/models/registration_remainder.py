
import time

class RegistrationRemainderModel:

    def __init__(self):
        self._users_notification = {}

    def get(self, user_id):
        return self._users_notification.get(user_id, None)

    def add(self, user_id):
        self._users_notification[user_id] = time.time()