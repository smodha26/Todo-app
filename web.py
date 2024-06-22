import streamlit as st
import functions

todo_list = functions.get_todos()

st.title("Todo App")
st.subheader("This app is to increase your productivity ! Enjoy")

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo here...")

