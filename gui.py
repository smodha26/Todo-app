import FreeSimpleGUI as FSG

label = FSG.Text("Type in a to-do")
input_box = FSG.InputText(tooltip="Enter a todo")
add_button = FSG.Button("Add")

window = FSG.Window('To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()