class FAQ:

    def __init__(self, dao, question, answer):
        self.dao = dao
        self.question = question
        self.answer = answer

class FAQModel:

    RANGE_ID = 'Відповіді на запитання!A2:B'

    def __init__(self, service, sheet, cache_ttl):
        self._service = service
        self._sheet = sheet
        self._cache_ttl = cache_ttl
        self._data = self.load_data()

    def load_data(self):
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        data = [FAQ(self, question, answer) for question, answer in result]
        return data

    def get(self, force=False):
        return self._data

    def get_answer_by_question(self, question):
        for i in self._data:
            if i.question == question:
                return i
