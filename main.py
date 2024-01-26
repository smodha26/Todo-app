# Open and read the file at the beginning
with open('todos.txt', 'r') as read_file:
    todos = read_file.readlines()

while True:
    user_input = input("Type add, edit, show, delete or exit: ").strip()

    if user_input == "add":
        user_input = input("Add your todo:") + "\n"
        todos.append(user_input)
        print("Task added successfully.")

    elif user_input == "edit":
        if len(todos) == 0:
            print("The todos list is empty")
        else:
            for i, item in enumerate(todos, 1):
                print(f"{i} : {item.strip()}")
            index = int(input("Choose the index you want to edit: "))
            if 1 <= index <= len(todos):
                edited_task = input("Enter the edited task: ")
                todos[index - 1] = edited_task + '\n'  # Update the todo in the list
                print("Task edited successfully.")
            else:
                print("Invalid index. Please choose a valid index.")

    elif user_input == "show":
        if len(todos) == 0:
            print("The todos list is empty")
        else:
            for index, item in enumerate(todos, 1):
                print(f"{index} : {item.strip()}")

    elif user_input == "delete":
        if len(todos) == 0:
            print("The todos list is empty")
        else:
            for i, item in enumerate(todos, 1):
                print(f"{i} : {item.strip()}")
            index = int(input("Choose the index you want to delete: "))
            if 1 <= index <= len(todos):
                del todos[index - 1]
                print("Task deleted successfully.")
            else:
                print("Invalid index. Please choose a valid index.")

    elif user_input == "exit":
        print("Saving changes and exiting...")
        with open('todos.txt', 'w') as file:
            for index, todo in enumerate(todos, 1):
                file.write(f"{index} - {todo}")
        print("Bye bye!")
        break

    else:
        print("Error, try again...")
