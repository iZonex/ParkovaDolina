class Screen:

    def match_context(self, text):
        return False

    @staticmethod
    def match(message):
        return False

    @staticmethod
    def in_line_match_pattern(query):
        return False