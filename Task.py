from helper import date_handler, link_handler
from psycopg2.extensions import adapt, AsIs

class Task:
    def __init__(self, course, description, due_date, due_time, links, created_by):
        super().__init__()
        self.course = course
        self.description = description
        self.due_date = date_handler(due_date)
        self.due_time = due_time
        self.links = link_handler(links)
        self.created_by = created_by

    def __repr__(self):
        return f"({self.course}, {self.description}, {self.due_date}, {self.due_time}, {self.links}, {self.created_by})"

    def __str__(self):
        return f"{self.course} {self.description} {self.due_date} {self.due_time} {self.links} {self.created_by}"

def adapt_task(task):
    course = adapt(task.course)
    description = adapt(task.description)
    due_date = adapt(task.due_date)
    due_time = adapt(task.due_time)
    links = adapt(task.links)
    created_by = adapt(task.created_by)
    return AsIs("(%s, %s, %s, %s, %s, %s)" % (course, description, due_date, due_time, links, created_by))

