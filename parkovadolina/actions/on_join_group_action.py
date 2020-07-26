from aiogram import types

class OnJoinGroupAction:

    TEXT = (
        "Ласкаво просимо вас {first_name} {last_name}!\n"
        "В чат групи інвесторів ЖК Паркова Долина!\n"
        "Будь ласка зв'яжіться зі мною {bot_name} перед початком спілкування.\n"
    )

    BOT_NAME = "@ParkValleyBot"

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    async def action(self, message):
        member = message.from_user
        text_body = self.TEXT.format(
            first_name=member.first_name or "",
            last_name=member.last_name or "",
            bot_name=self.BOT_NAME
        )
        await message.reply(text_body)