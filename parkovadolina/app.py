import os
import telebot
from telebot import types
from core.sheet_api import dao
from core.router import Router
from screens.router import routes, default_route
from actions.important_news_action import ImportantNewsAction

# https://docs.google.com/spreadsheets/d/1pdaG9ePKEtn1bvvghKdyl5cVD4A4S4UyxU8Ibo9e4hI/edit?usp=sharing

bot = telebot.TeleBot(os.getenv("BOT_KEY", "1340390485:AAF5UnF-GgncRT52D9MO6E6EoZ_J_0vnrZk"))

BOT_NAME = "@ParkValleyBot"

TEXTS = {
    "welcome": {
        "ukr": (
            "Ласкаво просимо вас {first_name} {last_name}!\n"
            "В чат групи інвесторів ЖК Паркова Долина!\n"
            "Будь ласка зв'яжіться зі мною {bot_name} перед початком спілкування.\n"
        )
    },
}

important_news_action = ImportantNewsAction(bot, dao).action

router = Router(bot, dao, default_route, routes)

@bot.message_handler(content_types=['new_chat_members'])
def on_user_joins(message):
    member = message.from_user
    text_body = TEXTS["welcome"]["ukr"].format(
        first_name=member.first_name,
        last_name=member.last_name,
        bot_name=BOT_NAME
    )
    bot.reply_to(message, text_body)

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