import time
from aiogram import types

class OnMessageWORegistrationAction:

    TEXT = (
        "Перепрошую {username}, але не могли б ви зі мною зв'язатися? {bot_name}\n"
    )

    BOT_NAME = "@ParkValleyBot"

    def __init__(self, bot, dao, time_delay=10):
        self.bot = bot
        self.dao = dao
        self.time_delay = time_delay

    def send_again_check(self, now_time, user_id):
        last_notification = self.dao.registraion_remained.get(user_id)
        if last_notification:
            if now_time - self.dao.registraion_remained.get(user_id) >= self.time_delay:
                return True
            else:
                return False
        return True

    async def action(self, message):
        now_time = time.time()
        member = message.from_user
        if self.dao.users.get_by_user_id(member.id) == None:
            if self.send_again_check(now_time, member.id):
                username = " ".join([member.first_name or "", member.last_name or ""])
                text_body = self.TEXT.format(
                    username=username,
                    bot_name=self.BOT_NAME
                )
                await message.reply(text_body)
                self.dao.registraion_remained.add(member.id)