import requests, unicodedata
import datetime

def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data= {"grant_type":"password", "username": "raphael@picsprod.fr", "password": "Remiraph31520&" },
        auth=(client_id, client_secret)
        )
    return response.json()["access_token"]

def get_from_api(url, headers):
    response = requests.get(
        url,
        headers=headers
    )
    return response.json()

def get_task(url, workspace_id, task_id, headers):
    url = url + "/" + workspace_id + "/tasks/" + task_id
    return get_from_api(url, headers)

def get_all_tasks(url, workspace_id, headers):
    url = url + "/" + workspace_id + "/tasks"
    response = get_from_api(url, headers) 
    return response

def string_to_time(date_string):
    return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")

def get_updated_tasks_since(url, workspace_id, headers, since):
    response = get_all_tasks(url, workspace_id, headers)
    updated = []
    last_update = string_to_time(since)
    for element in response:
        if element["updated_at"]:
            date_update = string_to_time(element["updated_at"])
            if date_update > last_update:
               updated.append(element)
        else: 
            if element["created_at"]:
                date_update = string_to_time (element["created_at"])
                if date_update > last_update:
                    updated.append(element)
    return updated

def extract_data_from_task(task): 
    data = {}
    data["name"] = task["name"] #key = value
    data["project"] = task["project"]
    data["start_date"] = task["start_date"]

def update_api(put_url, headers, data_to_update):
    response = requests.put(
        put_url,
        headers=headers,
        json=data_to_update
    )
    if response.status_code == 200 or response.status_code==201:
        updated_data = response.json()  # If the API returns updated data, parse the response as JSON
        print("Data updated successfully : ", updated_data)
    else:
        print("Error in API request. Status code : ", response.status_code, "error_message : ", response)

def create_through_api(post_url, headers, new_data):
    response = requests.post(
        post_url,
        headers=headers,
        json = new_data
    )
    if response.status_code == 200 or response.status_code == 201:
        updated_data = response.json()  # If the API returns updated data, parse the response as JSON
        print("Data created successfully : ", new_data)
    elif response.status_code == 422:
        return 
    else:
        print("Error in API request. Status code : ", response.status_code, "error_message : ", response.content)

def create_task_in_project(url, workspace_id, project_id, headers, task_data):
    url = url + "/" + workspace_id + "/tasks"
    task_data.update(
        {"project_id":project_id}
    )
    create_through_api(url, headers, task_data)

def display_task(task):
    print(f'Name : {task["name"]}, last_update : {task["updated_at"]}')

def display_all_tasks(tasks_list):
    for task in tasks_list:
        display_task(task)

### Dico Name_tag and tags

def read_tag_dictionnary(file_name):
    dico = {}
    with open(file_name, "r", encoding="utf-8") as my_file:
        line = my_file.readline()
        while line:
            line = line.split(":", 2)
            dico[line[0]] = line[1].strip() # strip = enlever le caractère de saut de ligne
            line = my_file.readline()
    return dico

def write_dicto_in_file(file_name, dico):
    with open(file_name, "w", encoding="utf-8") as my_file:
        for key in dico:
            my_file.write(f'{key}:{dico[key]}\n')

def get_tags_from_project(url, workspace_id, project_id, headers):
    url = url + "/" + workspace_id + "/plans/" + project_id + "/tags"
    return get_from_api(url, headers)

def display_tag(tag_list):
    for tag in tag_list:
        print(f'Project : ', tag)

def assign_a_tag_to_a_project(url, workspace_id, project_id, headers, tag_data):
    url = url + "/" + workspace_id + "/plans/" + project_id + "/tags"
    create_through_api(url, headers, tag_data)

def create_tags_dico_from_project(url, workspace_id, tag_project_id, headers):
    tags_list = get_tags_from_project(url, workspace_id, tag_project_id, headers)
    tags_dico = {}
    for tag in tags_list:
        name = tag["name"]
        color = tag["color_id"]
        tags_dico[name] = color
    return tags_dico

def create_and_write_tags(url, workspace_id, tag_project_id, headers, file_name):
    dico = create_tags_dico_from_project(url, workspace_id, tag_project_id, headers)
    write_dicto_in_file(file_name, dico)
    print("Tags_dictionnary updated")

def assign_tags_to_project_from_dico(url, workspace_id, project_id, tags_dico, headers):
    for key in tags_dico:
        data = {
            "name":key,
            "color_id":tags_dico[key]
        }
        assign_a_tag_to_a_project(url, workspace_id, project_id, headers, data)