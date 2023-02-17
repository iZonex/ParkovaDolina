from parkovadolina.models.activitys import ActivitysModel
from parkovadolina.models.building_plan import BuildingPlanModel
from parkovadolina.models.building_status import BuildingStatusModel
from parkovadolina.models.checked_group import CheckedGroupModel
from parkovadolina.models.faq import FAQModel
from parkovadolina.models.ig import IGModel
from parkovadolina.models.important_news import ImportantNewsModel
from parkovadolina.models.persons import PersonsModel
from parkovadolina.models.registration_remainder import \
    RegistrationRemainderModel
from parkovadolina.models.rules import RulesModel
from parkovadolina.models.session import SessionModel
from parkovadolina.models.users import UsersModel


class DAOStorage:

    def __init__(self):
        self._service = None
        self.rules = RulesModel(self._service)
        self.faq = FAQModel(self._service)
        self.ig = IGModel(self._service)
        self.users = UsersModel(self._service)
        self.persons = PersonsModel(self._service)
        self.activity = ActivitysModel(self._service)
        self.checked_group = CheckedGroupModel(self._service)
        self.important_news = ImportantNewsModel(self._service)
        self.building_plan = BuildingPlanModel(self._service)
        self.building_status_results = BuildingStatusModel(self._service)
        self.session = SessionModel()
        self.registraion_remained = RegistrationRemainderModel()
