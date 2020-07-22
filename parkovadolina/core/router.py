class AbstractRouter: pass


class Router(AbstractRouter):

    default_route=None
    authorized_routes=[]
    default_unauthorized_route=None
    unauthorized_routes=[]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.default_route = self.default_route(bot,dao) if self.default_route else None 
        self.authorized_routes = [i(bot,dao) for i in self.authorized_routes] if self.authorized_routes else None
        self.default_unauthorized_route = self.default_unauthorized_route(bot,dao) if self.default_unauthorized_route else None
        self.unauthorized_routes = [i(bot,dao) for i in self.unauthorized_routes] if self.unauthorized_routes else None

    def routing(self, message, routes, default_route):
        for i in routes:
            if isinstance(i, AbstractRouter):
                if i.match_pattern(message):
                    return i
            elif i.match(message):
                self.registration_context(i, message)
                i.screen(message)
                return i
        if default_route.match(message):
            self.registration_context(default_route, message)
            return default_route.screen(message)

    def registration_context(self, route, message):
        user = self.dao.users.get_by_user_id(message.from_user.id)
        if user:
            skip_context = getattr(route, "skip_context", None)
            if skip_context:
                if not skip_context(message.text):
                    user.register_context(message.text)
            else:
                user.register_context(message.text)

    def match_pattern(self, message):
        user = self.dao.users.get_by_user_id(message.from_user.id)
        if user:
            route = self.routing(message, self.authorized_routes, self.default_route)
            if route:
                return True
        elif self.default_unauthorized_route and self.unauthorized_routes:
            self.routing(message, self.unauthorized_routes, self.default_unauthorized_route)
            return True
        return False