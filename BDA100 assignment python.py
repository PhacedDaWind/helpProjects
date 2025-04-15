from datetime import datetime
class Task:
    def __init__(self, description, priority, dueDate, status):
        self.description = description
        self.priority = priority
        self.dueDate = dueDate
        self.status = status

    def setDescription(self, description):
        self.description = description

    def setPriority(self, priority):
        self.priority = priority
    
    def setDueDate(self, dueDate):
        self.dueDate = dueDate
    
    def setStatus(self, status):
        self.status = status

    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority
    
    def getDueDate(self):
        return self.dueDate
    
    def getStatus(self):
        return self.status
    
def addTask(taskDictionary):
    uniqueId = False
    descriptionLength = False
    validPriority = False
    validDate = False
    validStatus = False
    priorityList = ["high", "medium", "low"]
    statusList = ["pending", "completed"]

    # Validation for unique task id entered
    while uniqueId == False:    # Loop till user enters a unique id
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            print("Task ID already exists.")
            uniqueId = False
        else:
            uniqueId = True

    # Validation for description length
    while descriptionLength == False:
        description = input("Enter description: ")
        if len(description) > 54:
            print("Description length too long!")
            descriptionLength = False
        else:
            descriptionLength = True
    
    # Validation for priority
    while validPriority == False:
        priority = input("Enter priority (High, Medium, Low): ")
        priority = priority.lower()
        if priority not in priorityList:
            print("Please enter a valid priority")
            validPriority = False
        else:
            validPriority = True

    # Validation for date
    while validDate == False:
        dueDate = input("Enter due date (YYYY-MM-DD): ")
        try:
            dueDate = datetime.strptime(dueDate, '%Y-%m-%d').date()
            validDate = True
        except ValueError:
            print("Please enter a valid date (YYYY-MM-DD)")
            validDate = False
    
    # Validation for status
    while validStatus == False:
        status = input("Enter status (Pending/Completed): ")
        status = status.lower()
        if status not in statusList:
            print("Please enter a valid status")
            validStatus = False
        else:
            validStatus = True
    taskCreated = Task(description, priority.capitalize(), dueDate, status.capitalize())
    taskDictionary[taskId] = taskCreated    # Add new task into dictionary
    print(f"Task {taskId} added")

def markTaskAsCompleted(taskDictionary):
    if not taskDictionary:
        return
    taskFound = False
    while taskFound == False:
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            taskFound = True
            taskDictionary[taskId].setStatus("Completed")
        else:
            print("Task is not found")

def editTask(taskDictionary):
    if not taskDictionary:
        return
    descriptionLength = False
    validPriority = False
    validDate = False
    validStatus = False
    priorityList = ["high", "medium", "low"]
    statusList = ["pending", "completed"]
    taskFound = False

    # Validation for task id that exists
    while taskFound == False:
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            taskFound = True
        else:
            print("Task is not found")

    # Validation for description length
    while descriptionLength == False:
        description = input("Enter description: ")
        if len(description) > 54:
            print("Description length too long!")
            descriptionLength = False
        else:
            descriptionLength = True
    
    # Validation for priority
    while validPriority == False:
        priority = input("Enter priority (High, Medium, Low): ")
        priority = priority.lower()
        if priority not in priorityList:
            print("Please enter a valid priority")
            validPriority = False
        else:
            validPriority = True

    # Validation for date
    while validDate == False:
        dueDate = input("Enter due date (YYYY-MM-DD): ")
        try:
            dueDate = datetime.strptime(dueDate, '%Y-%m-%d').date()
            validDate = True
        except ValueError:
            print("Please enter a valid date (YYYY-MM-DD)")
            validDate = False
    
    # Validation for status
    while validStatus == False:
        status = input("Enter status (Pending/Completed): ")
        status = status.lower()
        if status not in statusList:
            print("Please enter a valid status")
            validStatus = False
        else:
            validStatus = True
    taskUpdated = Task(description, priority.capitalize(), dueDate, status.capitalize())
    taskDictionary.update({taskId : taskUpdated})    # Update task into dictionary
    print(f"Task {taskId} updated!")

def deleteTask(taskDictionary):
    if not taskDictionary:
        return
    taskFound = False
    while taskFound == False:
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            taskFound = True
        else:
            print("Task is not found")
    taskDictionary.pop(taskId)

def listTasks(taskDictionary):
    if not taskDictionary:
        print("Task list is empty.")
        return
    print("+-----------+-------------------------------------------------------+----------+----------------+-------------+")
    print("| Task ID   | Description                                           | Priority | Due Date       | Status      |")
    print("+-----------+-------------------------------------------------------+----------+----------------+-------------+")
    for k, v in taskDictionary.items():
        # Format each field with consistent spacing
        task_id = f"| {k.ljust(10)}"
        description = f"| {v.getDescription().ljust(54)}"
        priority = f"| {v.getPriority().ljust(9)}"
        due_date = f"| {str(v.getDueDate()).ljust(15)}"
        status = f"| {v.getStatus().ljust(12)}|"
        print(task_id + description + priority + due_date + status)
    print("+-----------+-------------------------------------------------------+----------+----------------+-------------+")

def filterTask(taskDictionary):
    if not taskDictionary:
        print("Task list is empty.")
        return
    print("\nFilter by:")
    print("1. Priority")
    print("2. Due Date Range")
    print("3. Status")
    print("4. Return to main menu")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    filteredTasks = {}
    
    if choice == 1:     # Filter by priority
        priorityList = ["high", "medium", "low"]
        validPriority = False
        print("\nPriority levels: High, Medium, Low")

        while validPriority == False:
            priority = input("Enter priority level to filter: ")
            if priority.lower() not in priorityList:
                print("Please enter a valid priority")
                validPriority = False
            else:
                validPriority = True
        for taskId, task in taskDictionary.items():
            if task.getPriority().lower() == priority.lower():
                filteredTasks[taskId] = task
    
    elif choice == 2:   # Filter by date range
        validStartDate = False
        validEndDate = False
        print("\nEnter date range (format: YYYY-MM-DD)")

        # Validation for dates
        while validStartDate == False:
            startDate = input("Start date: ")
            try:
                startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
                validStartDate = True
            except ValueError as e:
                print("Enter a valid date")
                validStartDate = False
            
        while validEndDate == False:
            endDate = input("End date: ")
            try:
                endDate = datetime.strptime(endDate, '%Y-%m-%d').date()
                validEndDate = True
            except ValueError as e:
                print("Enter a valid date")
                validEndDate = False
        
        # Find the tasks in between the dates
        for taskId, task in taskDictionary.items():
            if task.getDueDate() >= startDate and task.getDueDate() <= endDate:
                filteredTasks[taskId] = task
    
    elif choice == 3:   # Filter by status
        statusList = ["pending", "completed"]
        validStatus = False
        print("\nStatus options: Pending, Completed")
        
        # Status validation
        while validStatus == False:
            status = input("Enter status to filter: ")
            status = status.lower()
            if status.lower() not in statusList:
                print("Please enter a valid status")
                validStatus = False
            else:
                validStatus = True

        # Find by status
        for taskId, task in taskDictionary.items():
            if task.getStatus().lower() == status.lower():
                filteredTasks[taskId] = task
    
    elif choice == 4:  # Return to main menu
        return
    
    else:
        print("Invalid choice.")
        return
    
    if filteredTasks:   # if filteredTasks is not empty
        print("\nFiltered Tasks:")
        listTasks(filteredTasks)
    else:
        print("\nNo tasks matches your filter criteria.")

def saveToFile(taskDictionary):
    filename = input("Enter filename: ")
    try:
        with open(filename, "w") as file:
            for taskId, task in taskDictionary.items():
                line = f"{taskId}|{task.getDescription()}|{task.getPriority()}|{task.getDueDate()}|{task.getStatus()}\n"
                file.write(line)
        print(f"Tasks successfully saved to {filename}.")
    except Exception as e:
        print("Error while saving tasks:", str(e))

def loadFromFile(taskDictionary):
    filename = input("Enter filename to load: ")
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 5:
                    taskId, description, priority, dueDate, status = data
                    taskDictionary[taskId] = Task(description, priority, dueDate, status)
        print(f"Tasks successfully loaded from {filename}.")
        listTasks(taskDictionary)
    except FileNotFoundError:
        print(f"{filename} not found. Please check the filename and try again.")
    except Exception as e:
        print("Error while loading tasks:", str(e))


def main():
    taskDictionary = {}
    while True:
        print("1. Add New Task\n2. Mark Task as Completed\n3. Edit Task Details\n4. Delete Task\n5. Search Task\n6. Display Tasks\n7. Save file\n8. Load file\n9. Exit")
        try:
            userInput = int(input("Select a number (1-9): "))
        except ValueError as e:
            print("Please enter a valid value")
            userInput = None  # Equivalent to setting variable to null
        if userInput == 1:
            addTask(taskDictionary)
        elif userInput == 2:    # TODO add in checking for when list is empty
            listTasks(taskDictionary)
            markTaskAsCompleted(taskDictionary)
        elif userInput == 3:
            listTasks(taskDictionary)
            editTask(taskDictionary)
        elif userInput == 4:
            listTasks(taskDictionary)
            deleteTask(taskDictionary)
        elif userInput == 5:
            filterTask(taskDictionary)
        elif userInput == 6:
            listTasks(taskDictionary)
        elif userInput == 7:
            saveToFile(taskDictionary)
        elif userInput == 8:
            loadFromFile(taskDictionary)
        elif userInput == 9:
            break


main()