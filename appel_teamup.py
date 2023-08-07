from appel_teamup import*
from appel_toggl import*
import requests, unicodedata

def get_all_sub_calendars(url, calendar_key, headers): #renvoie une liste, où chaque élément de la liste = 1 sous calendrier
    url = url + "/" + calendar_key + "/subcalendars"
    result = get_from_api(url, headers)
    return result['subcalendars']

def display_all_sub_calendars(url, calendar_key, headers):
    result = get_all_sub_calendars(url, calendar_key, headers)
    for element in result:
        print(f'title : {element["name"]}, id : {element["id"]}')

def get_sub_calendar(url, calendar_key, sub_calendar_id, headers):
    url = url + "/" + calendar_key + "/" + "subcalendars" + "/" + sub_calendar_id
    result = get_from_api(url, headers)
    return result

def create_new_event(url, calendar_key, headers, payload):
    event_url = url + "/" + calendar_key + "/events"
    create_through_api(event_url, headers, payload)

#on va créer un parser qui va construire un dico associant
#à chaque nom, son id de calendrier teamUp
def associate_name_to_calendar_id(url, calendar_key, headers):
    result = get_all_sub_calendars(url, calendar_key, headers)
    dico = {}
    for element in result:
        name = element["name"].split(" ", 2)
        if name[0] =="TEAM":
            name = name[2]
            name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII').strip().lower()
            value = element["id"]
            dico[name]=value
    return dico