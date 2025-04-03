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
    while uniqueId == False:    # Loop till user enters a unique id
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            print("Task ID already exists.")
            uniqueId = False
        else:
            uniqueId = True
    description = input("Enter description: ")  # TODO add validation
    priority = input("Enter priority: ")
    dueDate = input("Enter due date: ")
    status = input("Enter status: ")
    taskCreated = Task(description, priority, dueDate, status)
    taskDictionary[taskId] = taskCreated    # Add new task into dictionary
    print(taskDictionary)

def markTaskAsCompleted(taskDictionary):
    taskFound = False
    while taskFound == False:
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            taskFound = True
            taskDictionary[taskId].setStatus("COMPLETED")
        else:
            print("Task is not found")

def editTask(taskDictionary):
    taskFound = False
    while taskFound == False:
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            taskFound = True
        else:
            print("Task is not found")
    description = input("Enter description: ")  # TODO add validation
    priority = input("Enter priority: ")
    dueDate = input("Enter due date: ")
    status = input("Enter status: ")
    taskUpdated = Task(description, priority, dueDate, status)
    taskDictionary.update({taskId : taskUpdated})    # Update task into dictionary

def deleteTask(taskDictionary):
    taskFound = False
    while taskFound == False:
        taskId = input("Enter Task ID: ")
        if taskId in taskDictionary:
            taskFound = True
        else:
            print("Task is not found")
    taskDictionary.pop(taskId)

def listTasks(taskDictionary):
    print("+-----------+-------------------------------------------------------+----------+----------------+-------------+")
    print("| Task ID   | Description                                           | Priority | Due Date       | Status      |")
    print("+-----------+-------------------------------------------------------+----------+----------------+-------------+")
    for k, v in taskDictionary.items():
        # Format each field with consistent spacing
        task_id = f"| {k.ljust(10)}"
        description = f"| {v.getDescription().ljust(54)}"
        priority = f"| {v.getPriority().ljust(9)}"
        due_date = f"| {v.getDueDate().ljust(15)}"
        status = f"| {v.getStatus().ljust(12)}|"
        print(task_id + description + priority + due_date + status)
    print("+-----------+-------------------------------------------------------+----------+----------------+-------------+")

def main():
    taskDictionary = {}
    while True:
        print("Select a number (1-9)")
        userInput = int(input("1. Add New Task\n2. Mark Task as Completed\n3. Edit Task Details\n4. Delete Task\n5. Search Task\n6. Display Tasks\n7. Save file\n8. Load file\n9. Exit"))
        if userInput == 1:
            addTask(taskDictionary)
        elif userInput == 2:    # TODO add in checking for when list is empty
            markTaskAsCompleted(taskDictionary)
        elif userInput == 3:
            editTask(taskDictionary)
        elif userInput == 4:
            deleteTask(taskDictionary)
        elif userInput == 6:
            listTasks(taskDictionary)
        elif userInput == 9:
            break


main()