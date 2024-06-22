import functions

# Initialize todos
todos = functions.get_todos()

# Print current time
now = functions.get_current_time()
print("Current time : " + now)

while True:
    user_input = input("Type add, edit, show, delete or exit: ").strip()

    if user_input == "add":
        user_input = input("Add your todo:").strip()
        todos = functions.add_task(todos, user_input)
        print("Task added successfully.")

    elif user_input == "edit":
        if len(todos) == 0:
            print("The todos list is empty")
        else:
            print(functions.show_tasks(todos))
            try:
                index = int(input("Choose the index you want to edit: "))
                edited_task = input("Enter the edited task: ").strip()
                todos = functions.edit_task(todos, index, edited_task)
                print("Task edited successfully.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except IndexError as e:
                print(e)

    elif user_input == "show":
        print(functions.show_tasks(todos))

    elif user_input == "delete":
        if len(todos) == 0:
            print("The todos list is empty")
        else:
            print(functions.show_tasks(todos))
            try:
                index = int(input("Choose the index you want to delete: "))
                todos = functions.delete_task(todos, index)
                print("Task deleted successfully.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except IndexError as e:
                print(e)

    elif user_input == "exit":
        print("Saving changes and exiting...")
        functions.write_todos(todos)
        print("Bye bye!")
        break

    else:
        print("Error, try again...")
