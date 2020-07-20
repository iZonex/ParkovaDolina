import os
import telebot
from core.sheet_api import dao
from core.router import Router
from screens.router import routes, default_route
from actions.important_news_action import ImportantNewsAction
from actions.on_join_action import OnJoinGroupAction

# https://docs.google.com/spreadsheets/d/1pdaG9ePKEtn1bvvghKdyl5cVD4A4S4UyxU8Ibo9e4hI/edit?usp=sharing

bot = telebot.TeleBot(
    os.getenv("BOT_KEY", "1340390485:AAF5UnF-GgncRT52D9MO6E6EoZ_J_0vnrZk"))

important_news_action = ImportantNewsAction(bot, dao).action
router = Router(bot, dao, default_route, routes)
on_join_action = OnJoinGroupAction(bot, dao)


@bot.message_handler(content_types=['new_chat_members'])
def on_user_joins(message):
    on_join_action.action(message)


@bot.message_handler(func=lambda message: True)
def main_actions(message):
    if message.chat.type == "private":
        private_chat(message)
    else:
        important_news_action(message)


def private_chat(message):
    router.match_pattern(message)


if __name__ == "__main__":
    bot.polling()
