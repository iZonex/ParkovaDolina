from parkovadolina.screens.communication.contacts_screen import ContactsScreen
from parkovadolina.core.router import Router
from .main_screen import CommunicationScreen
from .chats_list_screen import ChatsListScreen

class CommunicationRouter(Router):

    routes = (
        ChatsListScreen,
        ContactsScreen,
    )

    default_route = CommunicationScreen
