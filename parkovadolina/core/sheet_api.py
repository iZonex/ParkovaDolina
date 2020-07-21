import pickle
import socket
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from models.rules import RulesModel
from models.faq import FAQModel
from models.ig import IGModel
from models.users import UsersModel
from models.persons import PersonsModel
from models.activitys import ActivitysModel
from models.checked_group import CheckedGroupModel
from models.important_news import ImportantNewsModel


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


SPREADSHEET_ID = '1pdaG9ePKEtn1bvvghKdyl5cVD4A4S4UyxU8Ibo9e4hI'
dao = SpreadSheet(SPREADSHEET_ID)
