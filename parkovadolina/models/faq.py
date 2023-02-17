from .model import CSVModel


class FAQ:

    def __init__(self, dao, question, answer):
        self.dao = dao
        self.question = question
        self.answer = answer

class FAQModel(CSVModel):

    DB_NAME = "faq"

    def __init__(self, service):
        self._service = service
        self._data = self.load_data()

    def load_data(self):
        result = self.read_from_db()
        data = [FAQ(self, question, answer) for question, answer in result[1:]]
        return data

    def get(self, force=False):
        return self._data

    def get_answer_by_question(self, question):
        for i in self._data:
            if i.question == question:
                return i
