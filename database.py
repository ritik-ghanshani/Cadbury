import os
import psycopg2
from psycopg2.extensions import register_adapter
import config
from dotenv import load_dotenv
from Task import Task, adapt_task
register_adapter(Task, adapt_task)

def create_tables():
    execute(f"CREATE TABLE IF NOT EXISTS Tasks {config.TASK_TABLE} ;", None )

def add_task(task):
    command = f"INSERT INTO Tasks{config.TASK_COLUMNS} VALUES %s ;"
    execute(command, task)

def show_tasks_by_user(name):
    return execute_and_return("SELECT * FROM Tasks WHERE created_by=%s;", name)

def execute(sql_command, args):
    conn = connect_to_database()
    with conn.cursor() as cur:
        try:
            cur.execute(sql_command, (args,))
            conn.commit()
        except Exception as e:
            print(f"Error in {execute.__name__}: {e}", flush=True)
            print("Command failed.", flush=True)
    conn.close()

def execute_and_return(sql_command, args):
    conn = connect_to_database()
    with conn.cursor() as cur:
        try:
            cur.execute(sql_command, (args,))
            conn.commit()
            return cur.fetchall()
        except Exception as e:
            print(f"Error: in {execute_and_return.__name__} : {e}", flush=True)
            print("Command failed.", flush=True)
    conn.close()

def connect_to_database():
    try:
        load_dotenv()
        HOST = os.environ['HOST']
        USERNAME = os.environ['USERNAME']
        PASSWORD = os.environ['PASSWORD']
        DB_NAME = os.environ['DB_NAME']
        PORT = os.environ['PORT']

        conn = psycopg2.connect(host=HOST, port=PORT, user=USERNAME, password=PASSWORD, database=DB_NAME)
        create_tables()
        return conn

    except Exception as e:
        print(f"Error: {e}", flush=True)
        print("Could not connect to database.", flush=True)
        exit()
