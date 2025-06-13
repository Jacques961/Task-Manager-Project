import gradio as gr
import datetime
import os
import re
from Task import Task
from user import user
from ToDoList import ToDoList

# Global variables to store current user session
current_user = None
logged_in = False

def register_user(username, password):
    """Register a new user"""
    global current_user, logged_in
    
    if not username:
        return "Username is required", "", ""
    
    if not password:
        return "Password is required", "", ""
    
    # Validate password (5 characters with letters, digits, and symbols)
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).+$'
    if len(password) != 5 or not re.match(pattern, password):
        return "Password must be 5 characters with combination of letters, digits, and symbols", "", ""
    
    # Check if user already exists
    users_path = 'users.txt'
    if os.path.exists(users_path):
        with open(users_path, 'r') as f:
            for line in f:
                if len(line) > 0 and line.split()[1] == username:
                    return "Username already exists", "", ""
    
    # Create new user
    new_user = user(username, password)
    
    # Save to users file
    with open(users_path, 'a') as f:
        f.write(f'User {username} Password {password}\n')
    
    current_user = new_user
    logged_in = True
    current_user.loadTasks()
    
    return f"User {username} registered successfully!", username, "*** Login successful! You can now manage your tasks. ***"

def login_user(username, password):
    """Login existing user"""
    global current_user, logged_in
    
    if not username or not password:
        return "Username and password are required", "", ""
    
    users_path = 'users.txt'
    if not os.path.exists(users_path):
        return "No users found. Please register first.", "", ""
    
    with open(users_path, 'r') as f:
        for line in f:
            if len(line) > 0:
                parts = line.strip().split()
                if len(parts) >= 4 and parts[1] == username and parts[3] == password:
                    current_user = user(username, password)
                    logged_in = True
                    current_user.loadTasks()
                    return f"Welcome back, {username}!", username, "*** Login successful! You can now manage your tasks. ***"
    
    return "Invalid username or password", "", ""

def logout_user():
    """Logout current user"""
    global current_user, logged_in
    current_user = None
    logged_in = False
    return "Logged out successfully", "", ""

def get_tasks_display():
    """Get formatted display of all tasks"""
    if not logged_in or not current_user:
        return "Please login first"
    
    if current_user.getList().getTasksNumber() == 0:
        return "No tasks found"
    
    return current_user.__str__()

def add_new_task(title, description, due_date, priority, category):
    """Add a new task"""
    if not logged_in or not current_user:
        return "Please login first", get_tasks_display()
    
    if not title or not description:
        return "Title and description are required", get_tasks_display()
    
    try:
        due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD", get_tasks_display()
    
    # Convert priority and category to expected format
    priority_map = {"Low": "L", "Medium": "M", "High": "H"}
    category_map = {"Work": "work", "Personal": "personal", "Shopping": "shopping", "Other": "other"}
    
    priority_code = priority_map.get(priority, "M")
    category_code = category_map.get(category, "other")
    
    task = Task(
        current_user.getList().getTasksNumber(),
        title,
        description,
        due_date_obj,
        priority_code,
        category_code
    )
    
    current_user.getList().addTaskFromFile(task)
    current_user.saveTasks()
    
    return f"Task '{title}' added successfully!", get_tasks_display()

def delete_task(task_index, password_confirm):
    """Delete a task by index"""
    if not logged_in or not current_user:
        return "Please login first", get_tasks_display()
    
    if password_confirm != current_user.getPassword():
        return "Incorrect password", get_tasks_display()
    
    try:
        index = int(task_index)
        if index < 1 or index > current_user.getList().getTasksNumber():
            return "Invalid task index", get_tasks_display()
        
        current_user.getList().removeTask(index)
        current_user.saveTasks()
        return f"Task {index} deleted successfully!", get_tasks_display()
    
    except ValueError:
        return "Task index must be a number", get_tasks_display()

def mark_task_complete(task_index):
    """Mark a task as complete"""
    if not logged_in or not current_user:
        return "Please login first", get_tasks_display()
    
    try:
        index = int(task_index)
        if index < 1 or index > current_user.getList().getTasksNumber():
            return "Invalid task index", get_tasks_display()
        
        current_user.getList().markTaskDone(index)
        current_user.saveTasks()
        return f"Task {index} marked as complete!", get_tasks_display()
    
    except ValueError:
        return "Task index must be a number", get_tasks_display()

def check_overdue_task(task_index):
    """Check if a task is overdue"""
    if not logged_in or not current_user:
        return "Please login first", get_tasks_display()
    
    try:
        index = int(task_index)
        if index < 1 or index > current_user.getList().getTasksNumber():
            return "Invalid task index", get_tasks_display()
        
        result = current_user.getList().checkIfOverdue(index)
        if result:
            current_user.saveTasks()
            return f"Task {index} is overdue and has been updated!", get_tasks_display()
        else:
            return f"Task {index} is not overdue", get_tasks_display()
    
    except ValueError:
        return "Task index must be a number", get_tasks_display()

def update_task(task_index, new_title, new_description, new_due_date, new_priority, new_category):
    """Update an existing task"""
    if not logged_in or not current_user:
        return "Please login first", get_tasks_display()
    
    try:
        index = int(task_index)
        if index < 1 or index > current_user.getList().getTasksNumber():
            return "Invalid task index", get_tasks_display()
        
        task = current_user.getList()._ToDoList__todolist[index-1]
        
        if new_title:
            task.setTitle(new_title)
        
        if new_description:
            task.setDescription(new_description)
        
        if new_due_date:
            try:
                due_date_obj = datetime.datetime.strptime(new_due_date, "%Y-%m-%d")
                task.setDuedate(due_date_obj)
            except ValueError:
                return "Invalid date format. Use YYYY-MM-DD", get_tasks_display()
        
        if new_priority:
            priority_map = {"Low": "L", "Medium": "M", "High": "H"}
            task.setPriority(priority_map.get(new_priority, "M"))
        
        if new_category:
            category_map = {"Work": "work", "Personal": "personal", "Shopping": "shopping", "Other": "other"}
            task.setCategory(category_map.get(new_category, "other"))
        
        current_user.saveTasks()
        return f"Task {index} updated successfully!", get_tasks_display()
    
    except ValueError:
        return "Task index must be a number", get_tasks_display()

def filter_by_status(status):
    """Filter tasks by status"""
    if not logged_in or not current_user:
        return "Please login first"
    
    status_map = {"Completed": "Completed.", "Assigned": "Assigned.", "Overdue": "Overdue."}
    status_key = status_map.get(status, "Assigned.")
    
    filtered_tasks = ""
    count = 0
    for i, task in enumerate(current_user.getList()._ToDoList__todolist, 1):
        if task.getStatus() == status_key:
            filtered_tasks += f"\nTask {i}: {task.__str__()}\n"
            count += 1
    
    if count == 0:
        return f"No tasks found with status: {status}"
    
    return f"Tasks with status '{status}' ({count} found):\n{filtered_tasks}"

def filter_by_priority(priority):
    """Filter tasks by priority"""
    if not logged_in or not current_user:
        return "Please login first"
    
    filtered_tasks = ""
    count = 0
    for i, task in enumerate(current_user.getList()._ToDoList__todolist, 1):
        if task.getPriority() == priority:
            filtered_tasks += f"\nTask {i}: {task.__str__()}\n"
            count += 1
    
    if count == 0:
        return f"No tasks found with priority: {priority}"
    
    return f"Tasks with priority '{priority}' ({count} found):\n{filtered_tasks}"

def clear_all_tasks(password_confirm):
    """Clear all tasks"""
    if not logged_in or not current_user:
        return "Please login first", get_tasks_display()
    
    if password_confirm != current_user.getPassword():
        return "Incorrect password", get_tasks_display()
    
    current_user.getList().clearTasks()
    current_user.clearTasksFromFile()
    return "All tasks cleared successfully!", get_tasks_display()

# Create Gradio Interface
def create_interface():
    with gr.Blocks(title="Task Manager", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 📝 Personal Task Manager")
        
        # Login/Register Section
        with gr.Tab("🔐 Login/Register"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Login")
                    login_username = gr.Textbox(label="Username", placeholder="Enter your username")
                    login_password = gr.Textbox(label="Password", type="password", placeholder="Enter your password")
                    login_btn = gr.Button("Login", variant="primary")
                    
                with gr.Column():
                    gr.Markdown("### Register New Account")
                    reg_username = gr.Textbox(label="Username", placeholder="Choose a username")
                    reg_password = gr.Textbox(label="Password", type="password", 
                                            placeholder="5 chars: letters, digits, symbols")
                    register_btn = gr.Button("Register", variant="secondary")
            
            with gr.Row():
                auth_status = gr.Textbox(label="Status", interactive=False)
                current_user_display = gr.Textbox(label="Current User", interactive=False)
                login_status = gr.Textbox(label="Login Status", interactive=False)
            
            logout_btn = gr.Button("Logout", variant="stop")
        
        # Task Management Section
        with gr.Tab("📋 View Tasks"):
            refresh_btn = gr.Button("Refresh Tasks", variant="secondary")
            tasks_display = gr.Textbox(label="Your Tasks", lines=15, interactive=False)
            
        with gr.Tab("➕ Add Task"):
            with gr.Row():
                with gr.Column():
                    task_title = gr.Textbox(label="Task Title", placeholder="Enter task title")
                    task_description = gr.Textbox(label="Description", lines=3, placeholder="Enter task description")
                    task_due_date = gr.Textbox(label="Due Date (YYYY-MM-DD)", placeholder="2024-12-31")
                
                with gr.Column():
                    task_priority = gr.Dropdown(["Low", "Medium", "High"], label="Priority", value="Medium")
                    task_category = gr.Dropdown(["Work", "Personal", "Shopping", "Other"], label="Category", value="Personal")
                    add_task_btn = gr.Button("Add Task", variant="primary")
            
            add_task_status = gr.Textbox(label="Status", interactive=False)
        
        with gr.Tab("✏️ Update Task"):
            with gr.Row():
                with gr.Column():
                    update_task_index = gr.Textbox(label="Task Index", placeholder="Enter task number")
                    update_title = gr.Textbox(label="New Title (optional)", placeholder="Leave blank to keep current")
                    update_description = gr.Textbox(label="New Description (optional)", placeholder="Leave blank to keep current")
                
                with gr.Column():
                    update_due_date = gr.Textbox(label="New Due Date (optional)", placeholder="YYYY-MM-DD or leave blank")
                    update_priority = gr.Dropdown([None, "Low", "Medium", "High"], label="New Priority (optional)")
                    update_category = gr.Dropdown([None, "Work", "Personal", "Shopping", "Other"], label="New Category (optional)")
            
            update_task_btn = gr.Button("Update Task", variant="primary")
            update_task_status = gr.Textbox(label="Status", interactive=False)
        
        with gr.Tab("🗑️ Delete/Complete Tasks"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Mark Task Complete")
                    complete_task_index = gr.Textbox(label="Task Index", placeholder="Enter task number")
                    complete_btn = gr.Button("Mark Complete", variant="secondary")
                
                with gr.Column():
                    gr.Markdown("### Delete Task")
                    delete_task_index = gr.Textbox(label="Task Index", placeholder="Enter task number")
                    delete_password = gr.Textbox(label="Password", type="password", placeholder="Confirm with password")
                    delete_btn = gr.Button("Delete Task", variant="stop")
            
            task_action_status = gr.Textbox(label="Status", interactive=False)
        
        with gr.Tab("🔍 Filter Tasks"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Filter by Status")
                    status_filter = gr.Dropdown(["Completed", "Assigned", "Overdue"], label="Status")
                    filter_status_btn = gr.Button("Filter by Status")
                
                with gr.Column():
                    gr.Markdown("### Filter by Priority")
                    priority_filter = gr.Dropdown(["Low", "Medium", "High"], label="Priority")
                    filter_priority_btn = gr.Button("Filter by Priority")
            
            filter_results = gr.Textbox(label="Filtered Results", lines=10, interactive=False)
        
        with gr.Tab("🧹 Management"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Check Overdue")
                    overdue_task_index = gr.Textbox(label="Task Index", placeholder="Enter task number")
                    check_overdue_btn = gr.Button("Check if Overdue")
                
                with gr.Column():
                    gr.Markdown("### Clear All Tasks")
                    clear_password = gr.Textbox(label="Password", type="password", placeholder="Confirm with password")
                    clear_all_btn = gr.Button("Clear All Tasks", variant="stop")
            
            management_status = gr.Textbox(label="Status", interactive=False)
        
        # Event handlers
        login_btn.click(login_user, [login_username, login_password], [auth_status, current_user_display, login_status])
        register_btn.click(register_user, [reg_username, reg_password], [auth_status, current_user_display, login_status])
        logout_btn.click(logout_user, [], [auth_status, current_user_display, login_status])
        
        refresh_btn.click(get_tasks_display, [], [tasks_display])
        add_task_btn.click(add_new_task, [task_title, task_description, task_due_date, task_priority, task_category], [add_task_status, tasks_display])
        
        update_task_btn.click(update_task, [update_task_index, update_title, update_description, update_due_date, update_priority, update_category], [update_task_status, tasks_display])
        
        complete_btn.click(mark_task_complete, [complete_task_index], [task_action_status, tasks_display])
        delete_btn.click(delete_task, [delete_task_index, delete_password], [task_action_status, tasks_display])
        
        filter_status_btn.click(filter_by_status, [status_filter], [filter_results])
        filter_priority_btn.click(filter_by_priority, [priority_filter], [filter_results])
        
        check_overdue_btn.click(check_overdue_task, [overdue_task_index], [management_status, tasks_display])
        clear_all_btn.click(clear_all_tasks, [clear_password], [management_status, tasks_display])
    
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=True, debug=True)