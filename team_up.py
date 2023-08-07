from appel_toggl import* 
from appel_teamup import *
login = "contact@picsprod.fr"
password = "PPV2022r2@"
api_key = "dcb52e097b18e4260b0f8ce934d25b75239a99ecb50a0aa836e32dab265b6401"

teamup_api_url = "https://api.teamup.com"

headers = {
    "Teamup-Token": api_key,
    "Teamup_login": login,
    "Teamup_Password": password,
    "Content-Type": "application/json"
}

calendar_yvan_id = "12187366"
last_update = "2023-08-03T14:00:00"
calendar_key = "ksby28bgo5zzfbzu2k"

url_test = "https://api.teamup.com/ksby28bgo5zzfbzu2k/subcalendars"

data = {
    "subcalendar_ids" : [calendar_yvan_id],
    "start_dt" : "2023-08-02T08:00:00",
    "end_dt" : "2023-08-02T09:00:00",
    "title": "Test_task",
}

print(associate_name_to_calendar_id(teamup_api_url, calendar_key, headers))