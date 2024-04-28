import tasklist
import check_input

def main_menu():
    """return user's valid input for main menu"""
    print("1. Display current task")
    print("2. Display all taks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    return check_input.get_int_range("enter choice: ", 1, 6)

def get_date():
    """return the inputted date as a string in format MM/DD/YYYY"""
    mon = check_input.get_int_range("Enter month: ", 1, 12)
    
    #no need to check for month less than 31
    day = check_input.get_int_range("Enter day: ", 1, 31)
    year = check_input.get_int_range("Enter year: ", 2000, 2100)
    if mon < 10:
        mon = "0" + str(mon)
    if day < 10 : 
        day = "0" + str(day)
    date = str(mon) + "/" + str(day) +"/" + str(year)
    return date

def get_time():
    """return the inputted time as a string in format HH:MM"""
    hour = check_input.get_int_range("Enter hour: ", 0, 23)
    min = check_input.get_int_range("Enter minute: ", 0, 59)
    if hour < 10: 
        hour = "0" + str (hour)
    if min < 10 : 
        min = "0" + str (min)
    time = str(hour) + ":" + str(min)
    return time

def main():
    #read file and store in list 
    task_list = tasklist.Tasklist()

    done = False
    while not done:
        print("-Tasklist-")
        print("Tasks to complete: " + str(len(task_list)))
        choice = main_menu()

        #display current task
        if choice == 1:
            if len(task_list) > 0 :
                print("Current task is: ")
                print(str(task_list.get_current_task()))
            else:
                print("Tasks complete!")
        
        #display all task
        if choice == 2:
            if len(task_list) > 0:
                print ("Tasks: ")
                for i, t in enumerate(task_list):
                    print(str(i+1) + ". " + str(t))
                else:
                    print("Task complete!")

        #mark complete
        elif choice == 3:
            if len(task_list) > 0:
                print("Marking current task as complete: ")
                print (str(task_list.mark_complete()))
                if len(task_list) > 0:
                    print("New current task is: ")
                    print(str(task_list.get_current_task()))
                else: 
                    print("Tasks Complete!")
            else:
                print("Tasks complete!")

        #add task
        elif choice == 4:
            taskname = input ("Enter a task: ")
            print("Enter due date: ")
            date = get_date()
            print("Enter time: ")
            time = get_time()
            task_list.add_task(taskname, date, time)

        #search by date
        elif choice == 5:
            print("Enter date to search: ")
            date = get_date()
            print("Tasks due on " + date + ": ")
            for i, t in enumerate(task_list):
                if t.date == date:
                    print(str(i+1) + ". " + str(t))

        #save and quit
        elif choice == 6:
            task_list.save_file()
            done = True
            print("Saving list...")
        print()

main()
