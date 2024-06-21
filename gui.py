import PySimpleGUI as sg  # Assuming you meant PySimpleGUI
import functions

# Load initial todos
todos = functions.read_todos()

# Define the layout of the window
layout = [
    [sg.Text("To-Do List", font=('Helvetica', 20))],
    [sg.Listbox(values=todos, size=(40, 10), key='-LIST-', enable_events=True)],
    [sg.Text("Type in a to-do"), sg.InputText(tooltip="Enter a todo", key='-TODO-'), sg.Button("Add")],
    [sg.Button("Edit"), sg.Button("Delete")],
    [sg.Button("Exit")]
]

# Create the window
window = sg.Window('To-Do App', layout, font=('Helvetica', 15))

# Event loop
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        functions.write_todos(todos)  # Save todos before exiting
        break

    if event == 'Add':
        new_todo = values['-TODO-'].strip()
        if new_todo:
            todos = functions.add_task(todos, new_todo)
            window['-LIST-'].update(todos)
            window['-TODO-'].update("")

    elif event == '-LIST-' and values['-LIST-']:
        selected_task = values['-LIST-'][0]

    elif event == 'Edit':
        if values['-LIST-']:
            index = todos.index(values['-LIST-'][0])
            new_todo = values['-TODO-'].strip()
            if new_todo:
                todos = functions.edit_task(todos, index + 1, new_todo)
                window['-LIST-'].update(todos)
                window['-TODO-'].update("")

    elif event == 'Delete':
        if values['-LIST-']:
            index = todos.index(values['-LIST-'][0])
            todos = functions.delete_task(todos, index + 1)
            window['-LIST-'].update(todos)
            window['-TODO-'].update("")

window.close()
