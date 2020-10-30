from parkovadolina.screens.cameras_screen import CameraScreen
from parkovadolina.screens.air_clean_screen import AirCleanScreen
from parkovadolina.screens.services_screen import ServicesScreen
from parkovadolina.core.router import Router
from .important_news_screen import ImportantNewsScreen
from .main_screen import MainScreen
from .checked_group_screen import CheckedGroupScreen
from .faq_screen import FAQScreen
from .activitys_screen import ActivitysScreen
from .persons.router import PersonsRouter
from .ig_screen import IGScreen
from .building_progress.router import BuildingRouter
from .communication.router import CommunicationRouter
from .rules_screen import RulesScreen


class MainRouter(Router):

    root = True
    routes = (
        CameraScreen,
        CheckedGroupScreen,
        FAQScreen,
        ActivitysScreen,
        PersonsRouter,
        CommunicationRouter,
        IGScreen,
        ImportantNewsScreen,
        BuildingRouter,
        RulesScreen,
        ServicesScreen,
        AirCleanScreen,
    )

    default_route = MainScreen