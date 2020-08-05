from parkovadolina.models.registration_remainder import RegistrationRemainderModel
from parkovadolina.models.building_status import BuildingStatusModel
import pickle
import socket
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from parkovadolina.models.rules import RulesModel
from parkovadolina.models.faq import FAQModel
from parkovadolina.models.ig import IGModel
from parkovadolina.models.users import UsersModel
from parkovadolina.models.session import SessionModel
from parkovadolina.models.persons import PersonsModel
from parkovadolina.models.activitys import ActivitysModel
from parkovadolina.models.checked_group import CheckedGroupModel
from parkovadolina.models.important_news import ImportantNewsModel
from parkovadolina.models.building_plan import BuildingPlanModel

class SpreadSheet:

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly',
              'https://www.googleapis.com/auth/spreadsheets']

    def __init__(self, sheet_id):
        self._service = self._init_service()
        self.rules = RulesModel(self._service, sheet_id)
        self.faq = FAQModel(self._service, sheet_id)
        self.ig = IGModel(self._service, sheet_id)
        self.users = UsersModel(self._service, sheet_id)
        self.persons = PersonsModel(self._service, sheet_id)
        self.activity = ActivitysModel(self._service, sheet_id)
        self.checked_group = CheckedGroupModel(self._service, sheet_id)
        self.important_news = ImportantNewsModel(self._service, sheet_id)
        self.building_plan = BuildingPlanModel(self._service, sheet_id)
        self.building_status = BuildingStatusModel(self._service, sheet_id)
        self.session = SessionModel()
        self.registraion_remained = RegistrationRemainderModel()

    def _init_service(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        socket.setdefaulttimeout(600)
        service = build('sheets', 'v4', credentials=creds)
        return service.spreadsheets()


SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "1YcefukFGx7XKvT7oONpnn1nqDGpJUsP3CQdNCL8jt5w")
dao = SpreadSheet(SPREADSHEET_ID)
