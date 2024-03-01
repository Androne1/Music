import sqlite3
import datetime


def get_connection(func):
    def wrapper(cur=None):
        with sqlite3.connect("database.db") as conn:
            with conn.cursor() as cur:
                func(cur)
    return wrapper

def logger(record):
    with open("journal", "a", encoding = "utf-8") as file:
        file.write(str(datetime.datetime.now()) + record + "\n")

@get_connection
def create_table_songs(cur=None):
    cur.execute("""
                create table if not exists music
                (
	                song_id int primary key,
	                song_name text not null,
	                mood text
                )
                """)
    logger("Таблица успешно создна")
    
create_table_songs()