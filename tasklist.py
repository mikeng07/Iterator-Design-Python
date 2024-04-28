import task

class Tasklist:
    """
    List of Tasks
    Attributes:
    tasklist: Task [] - the list of tasks
    """

    def __init__(self):
        """initialize the list from a file"""
        self._tasklist = []
        file = open("tasklist.txt")
        for line in file:
            item = line.strip().split(",")
            t = task.Task(item[0],item[1],item[2])
            self._tasklist.append(t)
        self._tasklist.sort()

    def add_task (self, desc , date , time):
        """add new task to list"""
        self._tasklist.append(task.Task(desc,date,time))
        self._tasklist.sort()

    def get_current_task(self):
        return self._tasklist[0]
    
    def mark_complete(self):
        #remove current task
        return self._tasklist.pop(0)
    
    def save_file(self):
        #write content of tasklist to file
        file = open("tasklist.txt", "w")
        if len(self._tasklist) > 0:
            for t in range(len(self._tasklist) - 1):
                file.write(repr(self._tasklist[t]) + "\n")
            file.write(repr(self._tasklist[len(self._tasklist) - 1]))
        file.close()

    def __len__(self):
        """return number of task in the list"""
        return len(self._tasklist)

    def __iter__(self):
        """initialize and return iterator"""
        self._n = -1
        return self
    
    def __next__(self):
        """return next task in iteration until it reaches the end of the list"""
        self._n += 1
        if self._n >= len(self._tasklist):
            raise StopIteration
        else:
            return self._tasklist[self._n]