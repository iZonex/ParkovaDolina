import os
import telebot
from telebot import types
from core.sheet_api import dao
from screens.important_news_screen import ImportantNewsScreen
from screens.main_screen import MainScreen
from screens.checked_group_screen import CheckedGroupScreen
from screens.faq_screen import FAQScreen
from screens.building_activitys_screen import BuildingActivitysScreen
from screens.persons_screen import PersonsScreen
from screens.rules_screen import RulesScreen
from screens.communication_screen import CommunicationScreen
from screens.chats_list_screen import ChatsListScreen
from screens.forum_screen import ForumScreen
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

main_screen = MainScreen(bot,dao).screen
checked_group_screen = CheckedGroupScreen(bot, dao).screen
faq_screen = FAQScreen(bot, dao).screen
building_activitys_screen = BuildingActivitysScreen(bot, dao).screen
persons_screen = PersonsScreen(bot, dao).screen
rules_screen = RulesScreen(bot, dao).screen
communcation_screen = CommunicationScreen(bot, dao).screen
chats_list_screen = ChatsListScreen(bot, dao).screen
forum_screen = ForumScreen(bot, dao).screen
important_news_screen = ImportantNewsScreen(bot, dao).screen
important_news_action = ImportantNewsAction(bot, dao).action

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
    if message.text.startswith("Група підтверджених інвесторів"):
        checked_group_screen(message)
    elif message.text.startswith("Персона,") or message.text.startswith("Персони"):
        persons_screen(message)
    elif message.text.startswith("Правила"):
        rules_screen(message)
    elif message.text.startswith("🏁 Згоден з правилами"):
        rules_screen(message)
        main_screen(message)
    elif message.text.startswith("Важливі новини"):
        important_news_screen(message)
    elif message.text.startswith("Форум інвесторів"):
        forum_screen(message)
    elif message.text.startswith("Чати інвесторів") or  message.text.startswith("Чат"):
        chats_list_screen(message)
    elif message.text.startswith("Активності"):
        building_activitys_screen(message)
    elif message.text.startswith("Комунікація"):
        communcation_screen(message)
    elif message.text.startswith("Запитання,") or message.text.startswith("Відповіді на запитання"):
        faq_screen(message)
    else:
        main_screen(message)


if __name__ == "__main__":
    bot.polling()