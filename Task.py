from helper import date_handler, link_handler
from psycopg2.extensions import adapt, AsIs

class Task(object):
    def __init__(self, Course, Description, Due_date, Due_time, Links, Created_by):
        super().__init__()
        self.Course = Course
        self.Description = Description
        self.Due_date = date_handler(Due_date)
        self.Due_time = Due_time
        self.Links = link_handler(Links)
        self.Created_by = Created_by

    def __repr__(self):
        return f"({self.Course}, {self.Description}, {self.Due_date}, {self.Due_time}, {self.Links}, {self.Created_by})"

def adapt_task(task):
    Course = adapt(task.Course)
    Description = adapt(task.Description)
    Due_date = adapt(task.Due_date)
    Due_time = adapt(task.Due_time)
    Links = adapt(task.Links)
    Created_by = adapt(task.Created_by)
    return AsIs("(%s, %s, %s, %s, %s, %s)" % (Course, Description, Due_date, Due_time, Links, Created_by))

