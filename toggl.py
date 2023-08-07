import requests, base64, json
from appel_toggl import *
from appel_teamup import*
import datetime

last_update1 = "2023-08-07T08:00:00.00"

usrPass = "raphael@picsprod.fr:Remiraph31520&" #userid:password

get_token_url = "https://api.plan.toggl.com/api/v5/authenticate/token"
private_data = {"username" : "raphael@picsprod.fr", "password": "Remiraph31520&"}

app_key = "uIcwTwcziE" #client_id
secret = "3yS0NeL_gvCl_aPyxFlj"

toggl_plan_api = "https://api.plan.toggl.com/api/v5"
workspace_id = "672563"

access_token = get_access_token(get_token_url, app_key, secret)  #Donne le token d'accès à l'API, étape 1 !
access_token = "Bearer " + access_token

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

def add_task_project(url, headers):
    response = requests.post(
        url,
        headers=headers,
    )
    return response.json()

payload = {
     "name": "Test_task",
    "start_date": "2023-08-01",
    "end_date": "2023-08-02",
    "tag_ids":[158654]
}

tags_dico_file = "name_to_tag.txt"
#create_task_in_project(toggl_plan_api, workspace_id, test_api_id, header_put, payload)

#a = get_updated_tasks_since(toggl_plan_api, workspace_id,headers, last_update1)
#display_all_tasks(a)

test_api_id = "3003664"
test_api2 = "3006886"

tag_data = {
    "color_id": 30,
    "name": "Margot"
}

#assign_a_tag_to_a_project(toggl_plan_api, workspace_id, test_api2, headers, tag_data)

dico = create_tags_dico_from_project(toggl_plan_api, workspace_id, test_api_id, headers)
write_dicto_in_file(tags_dico_file, dico)
dico = read_tag_dictionnary(tags_dico_file)
assign_tags_to_project_from_dico(toggl_plan_api, workspace_id, test_api2, dico, headers)