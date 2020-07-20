class FAQ:

    def __init__(self, dao, question, answer):
        self.dao = dao
        self.question = question
        self.answer = answer

class FAQModel:

    RANGE_ID = 'Відповіді на запитання!A2:B'

    def __init__(self, service, sheet):
        self._service = service
        self._sheet = sheet
        self._data = []

    def get(self, force=False):
        result = self._service.values().get(spreadsheetId=self._sheet, range=self.RANGE_ID).execute().get('values', [])
        self._data = [FAQ(self, question, answer) for question, answer in result]
        return self._data

    def get_answer_by_question(self, question):
        for i in self._data:
            if i.question == question:
                return i
