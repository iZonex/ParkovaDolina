class AbstractRouter: pass


class Router(AbstractRouter):

    default_route=None
    routes=[]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.default_route = self.default_route(bot,dao) if self.default_route else None 
        self.routes = [i(bot,dao) for i in self.routes] if self.routes else []

    async def routing(self, message):
        self.registration_context(None, message)
        session = self.dao.session.get(message.from_user.id).get_context()
        if session and session[-1][0].match_context(message):
            route_screen = await session[-1][0].screen(message)
            return route_screen
        elif not session and message.text.startswith("↩️Назад"):
            self.registration_context(self.default_route, message)
            default_route_screen = await self.default_route.screen(message)
            return default_route_screen
        else:
            for route in self.routes:
                if isinstance(route, AbstractRouter):
                    match_patter = await route.match_pattern(message)
                    if match_patter:
                        return route
                elif route.match(message):
                    self.registration_context(route, message)
                    route_screen = await route.screen(message)
                    return route_screen
            if self.default_route.match(message):
                self.registration_context(self.default_route, message)
                default_route_screen = await self.default_route.screen(message)
                return default_route_screen

    async def in_line_routing(self, query):
        for route in self.routes:
            if isinstance(route, AbstractRouter):
                match_patter = await route.in_line_match_pattern(query)
                if match_patter:
                    return route
            elif route.in_line_match_pattern(query):
                route_in_line = await route.in_line(query)
                return route_in_line
        if self.default_route.in_line_match_pattern(query):
            default_in_line = await self.default_route.in_line(query)
            return default_in_line

    def registration_context(self, route, message):
        session = self.dao.session.get(message.from_user.id)
        skip_context = getattr(route, "skip_context", None)
        if skip_context:
            if not skip_context(message.text):
                session.register_context(route, message.text)
        else:
            session.register_context(route, message.text)

    async def match_pattern(self, message):
        route_found = await self.routing(message)
        if route_found:
            return True
        return False

    async def in_line_match_pattern(self, query):
        route_found = await self.in_line_routing(query)
        if route_found:
            return True
        return False

        