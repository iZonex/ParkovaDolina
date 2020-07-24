from core.router import Router
from .building_progress_screen import BuildingProgressScreen
from .main_screen import BuildingMainScreen

class BuildingRouter(Router):

    routes = (
        BuildingProgressScreen,
    )

    default_route = BuildingMainScreen
