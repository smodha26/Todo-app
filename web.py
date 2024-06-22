import streamlit as st
import functions

# Initialize session state for todos if not already initialized
if "todos" not in st.session_state:
    st.session_state.todos = functions.get_todos()


def add_todo():
    """Add a new todo to the list."""
    new_todo = st.session_state["new_todo"].strip()
    if new_todo:
        st.session_state.todos = functions.add_task(st.session_state.todos, new_todo)
        functions.write_todos(st.session_state.todos)
        st.session_state.new_todo = ""  # Clear the input field after adding


def delete_todo(todo):
    """Delete a todo from the list."""
    index = st.session_state.todos.index(todo)
    st.session_state.todos = functions.delete_task(st.session_state.todos, index + 1)
    functions.write_todos(st.session_state.todos)


def edit_todo():
    """Edit an existing todo."""
    if st.session_state.edit_index is not None:
        new_task = st.session_state["edit_todo"].strip()
        if new_task:
            st.session_state.todos = functions.edit_task(st.session_state.todos, st.session_state.edit_index + 1,
                                                         new_task)
            functions.write_todos(st.session_state.todos)
            st.session_state.edit_index = None  # Clear the edit index after editing
            st.session_state.edit_todo = ""  # Clear the edit input field


st.title("Todo App")
st.subheader("This app is to increase your productivity! Enjoy")

for i, todo in enumerate(st.session_state.todos):
    cols = st.columns([1, 4, 1, 1])
    with cols[0]:
        st.checkbox("", key=f"checkbox_{i}")
    with cols[1]:
        st.write(todo)
    with cols[2]:
        if st.button("Edit", key=f"edit_{i}"):
            st.session_state.edit_index = i
            st.session_state.edit_todo = todo
    with cols[3]:
        st.button("Delete", key=f"delete_{i}", on_click=delete_todo, args=(todo,))

if "edit_index" in st.session_state and st.session_state.edit_index is not None:
    st.text_input(label="", placeholder="Edit todo...", key='edit_todo', on_change=edit_todo)

st.text_input(label="", placeholder="Add a new todo here...", on_change=add_todo, key='new_todo')
