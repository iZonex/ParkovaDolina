from telebot import types

class ImportantNewsAction:

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    def action(self, message):
        if "#важливо" in message.text:
            self.dao.important_news.create(message.from_user.username, message.text, message.date)