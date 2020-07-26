import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from parkovadolina.core.sheet_api import dao
from parkovadolina.screens.router import MainRouter
from parkovadolina.actions.important_news_action import ImportantNewsAction
from parkovadolina.actions.on_join_group_action import OnJoinGroupAction

logging.basicConfig(level=logging.INFO)
API_TOKEN = os.getenv("BOT_KEY", "1300282330:AAH36oyCMrLwcB5te9G56KQS9-eq2Xt9Dzg")

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
    create_session(message)
    if message.chat.type == "private":
        await private_chat(message)
    else:
        important_news_action(message)

def create_session(message):
    user_id = message.from_user.id
    dao.session.create(user_id)

async def private_chat(message):
    await router.match_pattern(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)