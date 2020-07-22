from core.router import Router
from .communication_screen import CommunicationScreen
from .chats_list_screen import ChatsListScreen
from .forum_screen import ForumScreen

class CommunicationRouter(Router):

    authorized_routes = (
        ChatsListScreen,
        ForumScreen,
    )

    default_route = CommunicationScreen
