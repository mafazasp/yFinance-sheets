import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope =["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
   "credentials.json",
    scope
)

client = gspread.authorize(credentials)

sheet = client.open("yFinance-sheets").sheet1

data = sheet.get_all_records()

row = sheet.row_values(3)

insertRow = [1, "insert-test"]
sheet.insert_row(row, 2)

pprint(data)