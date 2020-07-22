from core.router import Router
from .main_screen import CommunicationScreen
from .chats_list_screen import ChatsListScreen
from .forum_screen import ForumScreen

class CommunicationRouter(Router):

    routes = (
        ChatsListScreen,
        ForumScreen,
    )

    default_route = CommunicationScreen
