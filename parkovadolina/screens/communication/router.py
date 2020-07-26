from parkovadolina.core.router import Router
from .main_screen import CommunicationScreen
from .chats_list_screen import ChatsListScreen
from .forum_screen import ForumScreen
from .voice_chats_screen import VoiceChatsScreen

class CommunicationRouter(Router):

    routes = (
        ChatsListScreen,
        ForumScreen,
        VoiceChatsScreen,
    )

    default_route = CommunicationScreen
