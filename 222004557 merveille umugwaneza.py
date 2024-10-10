
portfolio_changes = []  
project_queue = []      
client_projects = []    

def add_project(project_name):
   
    client_projects.append(project_name)
    portfolio_changes.append(('add', project_name))  
    print(f"Added project: {project_name}")

def remove_project(project_name):
    
    if project_name in client_projects:
        client_projects.remove(project_name)
        portfolio_changes.append(('remove', project_name))  
        print(f"Removed project: {project_name}")
    else:
        print(f"Project '{project_name}' not found.")

def submit_project(project_name):
   
    if project_name in client_projects:
        project_queue.append(project_name)
        print(f"Submitted project: {project_name}")
    else:
        print(f"Project '{project_name}' not found.")

def undo_change():
   
    if not portfolio_changes:
        print("No changes to undo.")
        return

    action, project_name = portfolio_changes.pop()
    if action == 'add':
        client_projects.remove(project_name)
        print(f"Undid addition of project: {project_name}")
    elif action == 'remove':
        client_projects.append(project_name)
        print(f"Undid removal of project: {project_name}")

def view_projects():
   
    print("Current Projects:", client_projects)

def view_submitted_projects():
    
    print("Submitted Projects:", project_queue)

if __name__ == "__main__":
    add_project("Website Redesign")
    add_project("Mobile App Development")
    view_projects()
    
    submit_project("Website Redesign")
    view_submitted_projects()
    
    remove_project("Mobile App Development")
    view_projects()
    
    undo_change()
    view_projects()


