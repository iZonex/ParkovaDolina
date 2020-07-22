from core.router import Router
from .main_screen import PersonsScreen
from .details_screen import PersonsDetailScreen

class PersonsRouter(Router):

    authorized_routes = (
        PersonsDetailScreen,
    )

    default_route = PersonsScreen
