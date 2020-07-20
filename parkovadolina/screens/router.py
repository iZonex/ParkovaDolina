from screens.important_news_screen import ImportantNewsScreen
from screens.main_screen import MainScreen
from screens.checked_group_screen import CheckedGroupScreen
from screens.faq_screen import FAQScreen
from screens.activitys_screen import ActivitysScreen
from screens.persons_screen import PersonsScreen
from screens.rules_screen import RulesScreen
from screens.communication_screen import CommunicationScreen
from screens.chats_list_screen import ChatsListScreen
from screens.forum_screen import ForumScreen
from screens.ig_screen import IGScreen

routes = (
    CheckedGroupScreen,
    FAQScreen,
    ActivitysScreen,
    PersonsScreen,
    RulesScreen,
    CommunicationScreen,
    ChatsListScreen,
    ForumScreen,
    IGScreen,
    ImportantNewsScreen
)

default_route = MainScreen