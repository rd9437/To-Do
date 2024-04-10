import streamlit as st
from datetime import datetime

# Function to add task
def add_task(list1):
    st.header("Add Task")
    task = st.text_input("Enter Task")
    dt = st.text_input("Due date (YYYY-MM-DD)")
    prit = st.selectbox("Priority", ["high", "medium", "low"])
    if st.button("Add Task"):
        try:
            dt = datetime.strptime(dt, "%Y-%m-%d")
            todo_list = {
                "Task": task,
                "Due Date": dt,
                "Priority": prit
            }
            list1.append(todo_list)
            st.success("Task added successfully!")
        except ValueError:
            st.error("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Function to view tasks
def view_tasks(list1):
    st.header("View Tasks")
    view = st.radio("View Options", ["All Tasks", "By Priority"])
    if view == "All Tasks":
        if list1:
            st.subheader("All Tasks:")
            for task in list1:
                st.write("Task:", task['Task'])
                st.write("Due Date:", task['Due Date'].strftime("%Y-%m-%d"))
                st.write("Priority:", task['Priority'])
                st.write("---")
        else:
            st.warning("No tasks found!")
    elif view == "By Priority":
        prit_filter = st.selectbox("Select Priority", ["high", "medium", "low"])
        filtered_tasks = [task for task in list1 if task['Priority'] == prit_filter]
        if filtered_tasks:
            st.subheader(f"Tasks with Priority {prit_filter.capitalize()}:")
            for task in filtered_tasks:
                st.write("Task:", task['Task'])
                st.write("Due Date:", task['Due Date'].strftime("%Y-%m-%d"))
                st.write("Priority:", task['Priority'])
                st.write("---")
        else:
            st.warning(f"No tasks found with priority {prit_filter.capitalize()}.")

# Function to edit tasks
def edit_task(list1):
    st.header("Edit Task")
    if list1:
        task_options = [task['Task'] for task in list1]
        task_to_edit = st.selectbox("Select Task to Edit", task_options)
        tindex = task_options.index(task_to_edit)
        tedit = list1[tindex]
        st.write("You chose to edit Task:", tedit['Task'])
        st.write("Due Date:", tedit['Due Date'].strftime("%Y-%m-%d"))
        st.write("Priority:", tedit['Priority'])
        new_task = st.text_input("Enter new task", value=tedit['Task'])
        new_due_date = st.text_input("Enter new due date (YYYY-MM-DD)", value=tedit['Due Date'].strftime("%Y-%m-%d"))
        new_priority = st.selectbox("Enter new priority", ["high", "medium", "low"], index=["high", "medium", "low"].index(tedit['Priority']))
        if st.button("Update Task"):
            try:
                new_due_date = datetime.strptime(new_due_date, "%Y-%m-%d")
                list1[tindex]['Task'] = new_task
                list1[tindex]['Due Date'] = new_due_date
                list1[tindex]['Priority'] = new_priority
                st.success("Task updated successfully!")
            except ValueError:
                st.error("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    else:
        st.warning("No tasks found!")

# Main function
def main():
    st.title("TaskPal")
    st.text("To-Do List")
    st.sidebar.title("Menu")
    
    # Initialize the list to store tasks
    if 'list1' not in st.session_state:
        st.session_state.list1 = []
    
    menu = st.sidebar.radio("Select Option", ["Add Task", "View Tasks", "Edit Task"])
    if menu == "Add Task":
        add_task(st.session_state.list1)
    elif menu == "View Tasks":
        view_tasks(st.session_state.list1)
    elif menu == "Edit Task":
        edit_task(st.session_state.list1)

if __name__ == "__main__":
    main()
