# Functions:
def view_tasks(task_dic):
    """For each task in the dictionary, print the task and its status"""
    for t in task_dic:
        if task_dic[t] == "incomplete":
            print(u"\u001b[31m")
            print(f"[]: {t}: {task_dic[t]}\u001b[0m")
        else:
            print(u"\u001b[32m")
            print(f"[]: {t}: {task_dic[t]}\u001b[0m")


def add_task(task_dict):
    """Takes a task input from the user and appends it to the task dictionary along with the status of the task. The default status is incomplete. Returns a view of the new list."""
    task_status = "incomplete"
    task_to_add = input("What is the task you need to add?: ").lower()
    task_dict.update({task_to_add: task_status})
    print("\nGreat! Here is your new to-do list:")
    view_tasks(task_dict)


def mark_complete(task_dict):
    """Takes the user's input and changes its status to complete. If the task is not already in the task dictionary, returns a key error. Returns a view of the user's to-do list."""
    try:
        task_to_mark = input("What is the task you need to mark complete?: ").lower()
        if task_to_mark not in task_dict:
            raise KeyError(task_to_mark)
    except KeyError:
        print(f"That task is not in the list.")
    else:
        tasks[task_to_mark] = "complete"
    finally:
        print("\nHere is your to-do list:")
        view_tasks(task_dict)


def delete_task(task_dict):
    """Takes the user's input and deletes it from the task dictionary. If the task is not in the dictionary, returns a key error. Returns a view of the user's to-do list."""
    try:
        task_to_delete = input("What is the task you need to delete?: ").lower()
        if task_to_delete not in task_dict:
            raise KeyError(task_to_delete)
    except KeyError:
        print(f"That task is not in the list.")
    else:
        task_dict.pop(task_to_delete)
    finally:
        print("\nHere is your to-do list:")
        view_tasks(task_dict)


def check_input(user_need, task_dict):
    """Takes the user's input and checks it to determine which action the app needs to take."""
    if user_need == "1" or user_need == "add a task":
        add_task(task_dict)
    elif user_need == "2" or user_need == "view tasks":
        view_tasks(task_dict)
    elif user_need == "3" or user_need == "mark a task complete":
        try:
            if len(tasks) == 0:
                raise KeyError
        except KeyError:
            print("There is nothing in the list. Please add something first.")
        else:
            mark_complete(task_dict)
    elif user_need == "4" or user_need == "delete a task":
        try:
            if len(tasks) == 0:
                raise KeyError
        except KeyError:
            print("There is nothing in the list. Please add something first.")
        else:
            delete_task(task_dict)
    else:
        print("Invalid input. Please try again.")


app_is_on = True
tasks = {
}
# User Interface - Welcome Message and Menu
print("Welcome to the To-Do List App!")
while app_is_on:
    menu = "Menu:\n 1. Add a task\n 2. View tasks\n 3. Mark a task complete\n 4. Delete a task\n 5. Quit"
    print(menu)
    # User chooses what they need to do.
    user_input = input("Choose a number from the menu: ").lower()
    # Check if user wants to quit first. If input = 5 or "quit", application should end.
    if user_input == "5" or user_input == "quit":
        app_is_on = False
    # If the input is not 5 or quit, run the check_input function to complete the desired function.
    else:
        check_input(user_input, tasks)
        # Ask user if they want to do something else with the application. If yes, go back to the top of the loop and display the menu again. If not, end the application.
        another_task = input("\nDo you need anything else? Y or N: ").lower()
        if another_task == "y":
            app_is_on = True
        elif another_task == "n":
            app_is_on = False
        else:
            print("Invalid input. Please try again.")
            another_task = input("\nDo you need anything else? Y or N: ").lower()
