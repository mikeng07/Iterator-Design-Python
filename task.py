class Task:
    """Represent of Task with a description and a due date
        Attributes:
        description(str)- description of the task
        dat(str) - due date of the task(MM/DD/YYYY)
        time(str) - time the task is due (in military time), time in format HH:MM    
    """

    def __init__(self, desc, date, time):
        """init a task, description of task, date and time of task"""
        self._description = desc
        self._date = date
        self._time = time

    @property
    def date(self):
        return self._date
    
    def __str__(self):
        return self._description + " - Due: " + self._date + " at " + self._time
    
    def __repr__(self):
        return self._description + "," + self._date + "," + self._time
    
    def __lt__(self,other):
        #return true if self date is less than other date
        #Compare by year, month, day, hour, minute, description in alphabet
        date_s = self._date.split("/")[2:] + self._date.split("/")[:2] + self._time.split(":") #[Y, M, D, H, M]
        date_o = other._date.split("/")[2:] + other._date.split("/")[:2] + other._time.split(":") #[Y, M, D, H, M]
        

        if date_s == date_o:
            return self._description.upper() < other._description.upper()
        else:
            return date_s < date_o