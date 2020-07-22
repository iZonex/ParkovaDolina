from core.router import Router
from .important_news_screen import ImportantNewsScreen
from .main_screen import MainScreen
from .checked_group_screen import CheckedGroupScreen
from .faq_screen import FAQScreen
from .activitys_screen import ActivitysScreen
from .persons.router import PersonsRouter
from .ig_screen import IGScreen
from .building_progress_screen import BuildingScreen
from .communication.router import CommunicationRouter
from .rules_screen import RulesScreen


class MainRouter(Router):

    root = True
    authorized_routes = (
        CheckedGroupScreen,
        FAQScreen,
        ActivitysScreen,
        PersonsRouter,
        CommunicationRouter,
        IGScreen,
        ImportantNewsScreen,
        BuildingScreen,
        RulesScreen,
    )

    default_route = MainScreen