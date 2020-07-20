class Router:

    def __init__(self, bot, dao, default_router, routes):
        self.default_router = default_router(bot,dao)
        self.routes = [i(bot,dao) for i in routes]

    def match_pattern(self, message):
        matched = False
        for i in self.routes:
            if i.match(message):
                i.screen(message)
                matched = True
        if not matched:
            self.default_router.screen(message)