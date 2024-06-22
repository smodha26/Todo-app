import time


def get_todos(file_path='todos.txt'):
    """Read todos from the file."""
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, file_path='todos.txt'):
    """Write todos to the file."""
    with open(file_path, 'w') as file:
        file.writelines(todos)


def get_current_time():
    """Return the current time as a formatted string."""
    return time.strftime("%b %d, %Y %H:%M:%S")


def add_task(todos, task):
    """Add a task to the todos list."""
    todos.append(task + '\n')
    return todos


def edit_task(todos, index, new_task):
    """Edit a task in the todos list."""
    if 1 <= index <= len(todos):
        todos[index - 1] = new_task + '\n'
        return todos
    else:
        raise IndexError("Invalid index. Please choose a valid index.")


def show_tasks(todos):
    """Return a formatted string of tasks."""
    if len(todos) == 0:
        return "The todos list is empty"
    else:
        return '\n'.join(f"{i} : {task.strip()}" for i, task in enumerate(todos, 1))


def delete_task(todos, index):
    """Delete a task from the todos list."""
    if 1 <= index <= len(todos):
        del todos[index - 1]
        return todos
    else:
        raise IndexError("Invalid index. Please choose a valid index.")