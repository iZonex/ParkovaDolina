from core.router import Router
from .main_screen import PersonsScreen
from .details_screen import PersonsDetailScreen

class PersonsRouter(Router):

    routes = (
        PersonsDetailScreen,
    )

    default_route = PersonsScreen
