import os
import psycopg2
import config
from dotenv import load_dotenv

try:
    load_dotenv()
    HOST = os.environ['HOST']
    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']
    DB_NAME = os.environ['DB_NAME']
    PORT = os.environ['PORT']

    conn = psycopg2.connect(host=HOST, port = PORT, user=USERNAME, password=PASSWORD, database=DB_NAME)

except Exception as e:
    print(f"Error: {e}", flush=True)
    print("Could not connect to database.", flush=True)
    exit()

def create_tables():
    execute(f"CREATE TABLE IF NOT EXISTS Tasks {config.TASK_TABLE};")

def add_task(class_name, description, due_date, due_time, links, name):
    command = f"INSERT INTO Tasks{config.TASK_COLUMNS} VALUES ('{class_name}', '{description}', '{due_date}', '{due_time}', '{links}', '{name}');"
    execute(command)


def show_tasks_by_user(name):
    tasks = execute_and_return(f"SELECT * FROM Tasks WHERE created_by='{name}';")

    

def execute(sql_command):
    with conn.cursor() as cur:
        try:
            cur.execute(sql_command)
            conn.commit()
        except Exception as e:
            print(f"Error: {e}", flush=True)
            print("Command failed.", flush=True)

def execute_and_return(sql_command):
    with conn.cursor() as cur:
        try:
            cur.execute(sql_command)
            return cur.fetchall()
            conn.commit()
        except Exception as e:
            print(f"Error: {e}", flush=True)
            print("Command failed.", flush=True)
