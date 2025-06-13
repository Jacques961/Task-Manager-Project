# 📝 Personal Task Manager

A comprehensive task management application built with Python, featuring both console and modern web interfaces. Manage your tasks efficiently with user authentication, priority settings, due date tracking, and more!

## ✨ Features

### 🔐 User Management
- **User Registration & Authentication**: Secure user accounts with password validation
- **Individual Task Lists**: Each user has their own isolated task environment
- **Password-Protected Actions**: Critical operations require password confirmation

### 📋 Task Management
- **Create Tasks**: Add tasks with title, description, due date, priority, and category
- **Update Tasks**: Modify existing tasks with new information
- **Delete Tasks**: Remove unwanted tasks with password confirmation
- **Mark Complete**: Track task completion status
- **Overdue Detection**: Automatically identify and mark overdue tasks

### 🎯 Organization Features
- **Priority Levels**: Low, Medium, High priority classification
- **Categories**: Work, Personal, Shopping, Other
- **Status Tracking**: Assigned, Completed, Overdue status management
- **Filtering**: View tasks by status or priority
- **Bulk Operations**: Clear all tasks at once

### 🖥️ Dual Interface
- **Console Interface**: Traditional command-line interaction
- **Web Interface**: Modern, user-friendly Gradio-based UI

## 🚀 Quick Start

### Prerequisites
```bash
python >= 3.7
pip install gradio
```

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   
   **Web Interface (Recommended):**
   ```bash
   python task_manager_ui.py
   ```
   Then open your browser to `http://127.0.0.1:7860`

   **Console Interface:**
   ```bash
   python task_manager.py
   ```

## 📁 Project Structure

```
task-manager/
│
├── 📄 Task.py                 # Task class definition
├── 📄 ToDoList.py            # Task list management
├── 📄 user.py                # User class and file operations
├── 📄 task_manager.py        # Console interface
├── 📄 task_manager_ui.py     # Web interface (Gradio)
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # This file
│
├── 📁 data/                  # Auto-generated data files
│   ├── users.txt            # User credentials
│   └── [username].txt       # Individual user task files
│
└── 📁 screenshots/          # UI screenshots
    ├── login.png
    ├── dashboard.png
    └── add_task.png
```

## 🎮 Usage Guide

### Web Interface

1. **Login/Register**
   - Create a new account or login with existing credentials
   - Password must be 5 characters with letters, digits, and symbols

2. **Managing Tasks**
   - **View Tasks**: See all your tasks in a formatted display
   - **Add Task**: Fill in task details and click "Add Task"
   - **Update Task**: Select task index and modify fields as needed
   - **Delete/Complete**: Mark tasks as done or remove them entirely

3. **Filtering & Organization**
   - Filter tasks by status (Assigned, Completed, Overdue)
   - Filter tasks by priority (Low, Medium, High)
   - Check for overdue tasks automatically

### Console Interface

Navigate through numbered menu options:
```
1. View the tasks
2. Add a task
3. Delete a task
4. Update a task
5. Check if task is overdue
6. Mark task as completed
7. Sort task by status
8. Sort task by priority
9. Clear all tasks
10. Go back to log in
0. Quit
```

## 🔧 Configuration

### File Locations
- **User Data**: Stored in text files in the project directory
- **Task Files**: Each user gets a separate `[username].txt` file
- **User Registry**: All users stored in `users.txt`

### Password Requirements
- Exactly 5 characters
- Must contain letters, digits, and symbols
- Example: `Ab3@9`

### Date Format
- All dates use `YYYY-MM-DD` format
- Example: `2024-12-31`

## 🎨 Screenshots

### Web Interface
![Login Screen](screenshots/login.png)
*User registration and login interface*

![Task Dashboard](screenshots/dashboard.png)
*Main task management dashboard*

![Add Task Form](screenshots/add_task.png)
*Task creation form with all options*

## 🏗️ Technical Architecture

### Core Classes

#### `Task` Class
- Handles individual task properties and validation
- Manages task status, priority, and category
- Provides formatted string representation

#### `ToDoList` Class
- Manages collections of tasks
- Implements task operations (add, remove, update)
- Handles filtering and sorting functionality

#### `user` Class
- Manages user authentication and data
- Handles file I/O for task persistence
- Provides user-specific task list access

### Data Persistence
- **File-based storage**: Simple text file format
- **User isolation**: Each user has a separate task file
- **Automatic backup**: Tasks saved after each operation

## 🔍 API Reference

### Key Methods

```python
# Task Management
task = Task(id, title, description, due_date, priority, category)
todo_list.addTask()
todo_list.removeTask(index)
todo_list.updateTask(index)

# User Operations
user.loadTasks()
user.saveTasks()
user.getList()

# Filtering
todo_list.sortByStatus(status)
todo_list.sortByPriority(priority)
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include error handling for user inputs
- Test both console and web interfaces

## 🐛 Known Issues & Limitations

- **File Locking**: Multiple users accessing simultaneously may cause conflicts
- **Path Dependencies**: Hardcoded paths may need adjustment for different systems
- **Session Management**: Web interface uses global variables (not production-ready)
- **No Database**: Uses file-based storage (not scalable for many users)

## 🔮 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Task sharing and collaboration
- [ ] Email notifications for due dates
- [ ] Calendar integration
- [ ] Mobile-responsive design improvements
- [ ] Task attachments and notes
- [ ] Recurring tasks support
- [ ] Task time tracking
- [ ] Export/Import functionality (CSV, JSON)
- [ ] Dark mode support

## 📊 Statistics

- **Lines of Code**: ~800+
- **Classes**: 3 core classes
- **Features**: 15+ task management features
- **Interfaces**: 2 (Console + Web)
- **File Types**: Python, Text

⭐ **Star this repository if you found it helpful!** ⭐

*Made with ❤️ and Python*
