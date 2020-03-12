import todoist
from colorama import init

from authorize import get_token
from collections import defaultdict

from temp_token import token
from colors import COLOR

init()

# Use this in productions and make sure to store token
# token = get_token()

api = todoist.TodoistAPI(token)
api.sync()


def display_all_tasks():
    inbox_id = None
    projects = {}   
    for project in api.state['projects']:
        projects[project['id']] = project
        if hasattr(project, 'inbox_project'):
            inbox_id = project['id']

    project_tasks = group_tasks_into_projects(api.state['items'])  # project_id : List of tasks
    
    for project_id in project_tasks:
        BOLD = COLOR['BOLD']
        RESET = COLOR['RESET']
        color = COLOR[projects[project_id]['color']]
        project_name = projects[project_id]['name']
        print(f'\n{BOLD}{color}{project_name} {RESET}')

        for task in project_tasks[project_id]:
            content = task['content']
            print(f'- {color}{content}{RESET}')

def group_tasks_into_projects(tasks):
    project_tasks = defaultdict(list)

    for task in tasks:
        project_tasks[task['project_id']].append(task)
    
    return project_tasks


if __name__ == "__main__":
    display_all_tasks()
    while True:
        print(input())