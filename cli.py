import todoist
from colorama import init

from authorize import get_token
from collections import defaultdict

from getch import getch
from temp_token import token
from colors import COLOR

init()

# Use this in productions and make sure to store token
# token = get_token()

api = todoist.TodoistAPI(token)
api.sync()


def display_all_tasks(count, first=True):
    inbox_id = None
    projects = {}
    everything = []

    for project in api.state['projects']:
        projects[project['id']] = project
        if hasattr(project, 'inbox_project'):
            inbox_id = project['id']

    project_tasks = group_tasks_into_projects(api.state['items'])  # project_id : List of tasks
    
    if first:
        spacing = '\n'
    else:
        spacing = '\033[B'

    for project_id in project_tasks:
        BOLD = COLOR['BOLD']
        RESET = COLOR['RESET']
        color = COLOR[projects[project_id]['color']]
        project_name = projects[project_id]['name']
        everything.append(f'{spacing}{BOLD}{color}{project_name} {RESET}')

        for task in project_tasks[project_id]:
            content = task['content']
            everything.append(f'\u2610 {color}{content}{RESET}')
    
    if first:
        end = '\n'
        flush = False
    else:
        end = '\033[E \033[K'
        flush = True
    
    

    for i, line in enumerate(everything):
        if i == len(everything) - count:
            print(COLOR['REVERSED'] + line, end=end, flush=flush)
        else:
            print(line, end=end, flush=flush)

    return len(everything) , len(projects)
        


def group_tasks_into_projects(tasks):
    project_tasks = defaultdict(list)

    for task in tasks:
        project_tasks[task['project_id']].append(task)
    
    return project_tasks


if __name__ == "__main__":
    n, spaces = display_all_tasks(0)
    
    count = 0
    while True:
        key = getch()

        # print(key.encode('utf-8'))
        if key == '\x03':
            break

        # Identify Arrow key presses
        if key == '\033':
            getch()
            press = getch()
            if press == 'A':
                if count == n:
                    continue

                print(f'\033[{n + spaces}A', end='', flush = True)
                count += 1 
                display_all_tasks(count, False)
            if press == 'B':
                if count == 1:
                    continue
                
                print(f'\033[{n + spaces}A', end='')
                count -= 1 
                display_all_tasks(count, False)
        
        
        