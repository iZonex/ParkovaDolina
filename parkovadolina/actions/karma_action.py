from aiogram import types

class OnKarmaAction:

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    async def get(self, message):
        text_body = "Idk"
        await message.reply(text_body)

    async def give(self, username, message):
        text_body = f"{username} +1 karma"
        await message.reply(text_body)

    async def withdraw(self, username, message):
        text_body = f"{username} -1 karma"
        await message.reply(text_body)

    async def action(self, message):
        print(message.md_text)
        username, action = message.text.split(" ")
        if "+" in action or "++" in action:
            await self.give(username, message)
        elif "-" in action or "—" in action:
            await self.withdraw(username, message)
        else:
            text_body = "Only -- and ++ available"
            await message.reply(text_body)