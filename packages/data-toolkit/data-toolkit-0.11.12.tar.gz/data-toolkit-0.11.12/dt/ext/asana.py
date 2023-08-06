import asana
import json
import os
# import request
import pandas as pd
import time

# pandas set max column width
pd.set_option('display.max_colwidth', 50)


def user_select_option(message, options):
    option_lst = list(options)
    print_(message)
    for i, val in enumerate(option_lst):
        print_(i, ': ' + val['name'])
    index = int(input("Enter choice (default 0): ") or 0)
    return option_lst[index]

def get_client():
    with open(os.path.expanduser('~/.dt_config.json')) as f:
        config = json.load(f)
        api_key = config['asana_api_key']
        
    # create asana client
    client = asana.Client.access_token(api_key)
    return client


def asana_list_todos(workspace_name,filtering):
    if filtering is None: filtering = 'due'
    
    df = asana_get_todos(workspace_name,filtering)
    df = df[['name',"due_on", "completed", "projects", "notes"]]
    
    if filtering == 'done':
        df = df[df['completed'] == True]
        print(df)
        
    if filtering == 'due':
        df = df[df['completed'] == False]
        print(df)
    
    if filtering == 'all':
        print(df)
        
def asana_get_todos(workspace_name,filtering):
     # read api key from ~/.dt_config.json
    client = get_client()
    (url, state) = client.session.authorization_url()
        
    me = client.users.me()
    workspace_id = me['workspaces'][0]['gid']
    
    # {'param': 'value', 'param': 'value'}
    # https://developers.asana.com/docs/get-tasks-from-a-project
    # print requests that python is making
    # import logging
    # logging.basicConfig(level=logging.DEBUG)

    opt_fields='name,due_on,completed,projects,notes'
    tasks = list(client.tasks.find_all({"opt_fields":opt_fields}, 
                                       workspace=workspace_id, assignee='me'))
    df = pd.DataFrame(tasks)
    return df
    
def add_todo(task_text, expected_duration, project_id=0):
    tm = time.localtime()
    
    if expected_duration is None:
        tar_date = f"{tm.tm_year}-{tm.tm_mon:02d}-{tm.tm_mday+1}"
    else:
        day = tm.tm_mday+int(expected_duration)
        tar_date = f"{tm.tm_year}-{tm.tm_mon:02d}-{day}"
    
    
    client = get_client()
    me = client.users.me()
    workspace_id = me['workspaces'][0]['gid']
    
    projects = list(client.projects.get_projects_for_workspace(workspace_id))
    
    # docs https://developers.asana.com/docs/create-a-task
        
    data =  {'name': task_text,
        "resource_subtype": "default_task",
        "assignee": me['gid'],
        "due_on": tar_date,
        "projects": projects[project_id]['gid'],
        # 'notes': 'Note: This is a test task created with the python-asana client.',
        # 'projects': [workspace_id]
    }
    
    result = client.tasks.create_in_workspace(workspace_id, data)

    print(json.dumps(result, indent=4))
    
def done_todo():
    pass


def fix_past_due(workspace_name):
    df = asana_get_todos(workspace_name,None)
    client = get_client()
    
    # select all that are past due
    df = df[df['completed'] == False]
    df = df[df['due_on'].notnull()]
    df['due_on'] = pd.to_datetime(df['due_on'])
    df = df[df['due_on'] < pd.Timestamp.today()]
    
    # asana update task to today
    all_tasks = []
    
    for i in df.index:
        task_id = df.loc[i,'gid']
        data =  {'due_on': pd.Timestamp.today().strftime("%Y-%m-%d")}
        result = client.tasks.update_task(task_id, data)
        # print(json.dumps(result, indent=4))
        all_tasks.append(result)
        
    df = pd.DataFrame(all_tasks)
    print(df)