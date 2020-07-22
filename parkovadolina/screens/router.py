from core.router import Router
from screens.important_news_screen import ImportantNewsScreen
from screens.main_screen import MainScreen
from screens.checked_group_screen import CheckedGroupScreen
from screens.faq_screen import FAQScreen
from screens.activitys_screen import ActivitysScreen
from screens.persons_screen import PersonsScreen
from screens.rules_screen import RulesScreen
from screens.ig_screen import IGScreen
from screens.building_progress_screen import BuildingScreen
from screens.unauthorized_menu_screen import UnathorizedMenuScreen
from screens.communication.router import CommunicationRouter


class MainRouter(Router):

    root = True
    authorized_routes = (
        CheckedGroupScreen,
        FAQScreen,
        ActivitysScreen,
        PersonsScreen,
        CommunicationRouter,
        IGScreen,
        ImportantNewsScreen,
        BuildingScreen
    )

    default_route = MainScreen

    unauthorized_routes = (
        RulesScreen,
    )

    default_unauthorized_route = UnathorizedMenuScreen