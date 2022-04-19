import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("steam-current-347705-ff9b76de4aef.json", scope)

client = gspread.authorize(creds)

sheet = client.open("This_is_gsheet2").sheet1

data = sheet.get_all_records()

print(data)



