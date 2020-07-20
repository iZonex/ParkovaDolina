from abc import abstractmethod

class BaseScreen:

    BASE_SECTIONS = ["🚪Вихід"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao