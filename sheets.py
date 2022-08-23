from pprint import pprint
from config import spreadsheet_id, client_id, api_key
import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from ozon_api import Ozon

CREDENTIALS_FILE = 'creds.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def append_titles(data):
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range='A1:A6', valueInputOption="RAW",
        body={'values': data}).execute()


title = [['action_type', 'title', 'date_start', 'date_end', 'description', 'id']]
append_titles(title)


def append_sheets(data):
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range='Лист1!A2', valueInputOption="RAW",
        body={'values': data}).execute()


def get_promo():
    ozon = Ozon(client_id, api_key)
    actions = ozon.get_actions()['result']
    for act in actions:
        actions_list = {'action_type': act['action_type'], 'title': act['title'], 'date_start': act['date_start'],
                        'date_end': act['date_end'], 'description': act['description'], 'id': act['id']}

        data = [[actions_list['action_type'], actions_list['title'], actions_list['date_start'],
                             actions_list['date_end'], actions_list['description'], actions_list['id']]]

        append_sheets(data)


get_promo()
