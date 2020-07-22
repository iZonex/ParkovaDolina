from core.router import Router
from .rules_screen import RulesScreen
from .unauthorized_menu_screen import UnathorizedMenuScreen

class CommunicationRouter(Router):

    unauthorized_routes = (
        RulesScreen,
    )

    default_unauthorized_route = UnathorizedMenuScreen