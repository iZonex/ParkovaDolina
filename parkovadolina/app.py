import os
from aiogram import Bot, Dispatcher, executor, types
from core.sheet_api import dao
from screens.router import MainRouter
from actions.important_news_action import ImportantNewsAction
from actions.on_join_group_action import OnJoinGroupAction

# https://docs.google.com/spreadsheets/d/1pdaG9ePKEtn1bvvghKdyl5cVD4A4S4UyxU8Ibo9e4hI/edit?usp=sharing

API_TOKEN = os.getenv("BOT_KEY", "1340390485:AAF5UnF-GgncRT52D9MO6E6EoZ_J_0vnrZk")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

important_news_action = ImportantNewsAction(bot, dao).action
router = MainRouter(bot, dao)
on_join_action = OnJoinGroupAction(bot, dao)


@dp.message_handler(content_types=['new_chat_members'])
async def on_user_joins(message):
    await on_join_action.action(message)


@dp.message_handler()
async def main_actions(message):
    if message.chat.type == "private":
        await private_chat(message)
    else:
        important_news_action(message)

def create_session(message):
    user_id = message.from_user.id
    dao.session.create(user_id)

async def private_chat(message):
    create_session(message)
    await router.match_pattern(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)