class Router:

    def __init__(self, bot, dao, default_route, authorized_routes, default_unauthorized_route, unauthorized_routes):
        self.bot = bot
        self.dao = dao
        self.default_route = default_route(bot,dao)
        self.default_unauthorized_route = default_unauthorized_route(bot,dao)
        self.authorized_routes = [i(bot,dao) for i in authorized_routes]
        self.unauthorized_routes = [i(bot,dao) for i in unauthorized_routes]


    def routing(self, message, routes, default_route):
        matched = False
        for i in routes:
            if i.match(message):
                i.screen(message)
                matched = True
        if not matched:
            default_route.screen(message)


    def match_pattern(self, message):
        user = self.dao.users.get_by_user_id(message.from_user.id)

        if user:
            self.routing(message, self.authorized_routes, self.default_route)
        else:
            self.routing(message, self.unauthorized_routes, self.default_unauthorized_route)
