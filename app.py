import logging
import os
from parkovadolina.actions.karma_action import OnKarmaAction
from parkovadolina.actions.on_ignore_registration import OnMessageWORegistrationAction
from aiogram import Bot, Dispatcher, executor, types
from parkovadolina.screens.router import MainRouter
from parkovadolina.actions.important_news_action import ImportantNewsAction
from parkovadolina.actions.on_join_group_action import OnJoinGroupAction
from parkovadolina.core.dao import DAOStorage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

STORAGE_CACHE_TTL = int(os.getenv("STORAGE_CACHE_TTL", 30))
API_TOKEN = os.getenv("BOT_KEY", "1300282330:AAH36oyCMrLwcB5te9G56KQS9-eq2Xt9Dzg")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "1YcefukFGx7XKvT7oONpnn1nqDGpJUsP3CQdNCL8jt5w")

dao = DAOStorage(SPREADSHEET_ID, STORAGE_CACHE_TTL)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

important_news_action = ImportantNewsAction(bot, dao)
router = MainRouter(bot, dao)
on_join_action = OnJoinGroupAction(bot, dao)
on_message_wo_registration = OnMessageWORegistrationAction(bot, dao)
on_karma_action = OnKarmaAction(bot, dao)

@dp.callback_query_handler() 
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await router.in_line_match_pattern(query)

@dp.message_handler(content_types=['new_chat_members'])
async def on_user_joins(message):
    await on_join_action.action(message)

def create_session(message):
    user_id = message.from_user.id
    dao.session.create(user_id)

async def middleware(message):
    create_session(message)
    if message.chat.type == "private":
        await private_chat_actions_middleware(message)
    else:
        await public_chat_actions_middleware(message)

async def public_chat_actions_middleware(message):
    await on_message_wo_registration.action(message)
    await important_news_action.action(message)
    await on_karma_action.action(message)

async def private_chat_actions_middleware(message):
    await router.match_pattern(message)

@dp.message_handler()
async def main_actions(message):
    await middleware(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)