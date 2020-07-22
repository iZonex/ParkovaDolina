class AbstractRouter: pass


class Router(AbstractRouter):

    default_route=None
    routes=[]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.default_route = self.default_route(bot,dao) if self.default_route else None 
        self.routes = [i(bot,dao) for i in self.routes] if self.routes else []

    def routing(self, message):
        for route in self.routes:
            if isinstance(route, AbstractRouter):
                if route.match_pattern(message):
                    return route
            elif route.match(message):
                self.registration_context(route, message)
                route.screen(message)
                return route
        if self.default_route.match(message):
            self.registration_context(self.default_route, message)
            return self.default_route.screen(message)

    def registration_context(self, route, message):
        user = self.dao.users.get_by_user_id(message.from_user.id)
        if user:
            skip_context = getattr(route, "skip_context", None)
            if skip_context:
                if not skip_context(message.text):
                    user.register_context(message.text)
            else:
                user.register_context(message.text)
            user.get_context()

    def match_pattern(self, message):
        if self.routing(message):
            return True
        return False