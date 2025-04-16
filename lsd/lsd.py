import os
import psycopg2
from time import sleep


GLOBAL_CONN = None
def establish_connection():
    global GLOBAL_CONN

    if GLOBAL_CONN is None:
        try:
            print(f"Going to try connecting with {os.environ.get('LSD_USER')} and {os.environ.get('LSD_API_KEY')}")
            GLOBAL_CONN = psycopg2.connect(
                host="localhost",
                database=os.environ.get("LSD_USER"),
                user=os.environ.get("LSD_USER"),
                password=os.environ.get("LSD_API_KEY"),
                port="5432",
            )
        except Exception as e:
            print("Ran into an issue connecting...")
            print(e)
            sleep(1)
            return establish_connection()

    try:
        with GLOBAL_CONN.cursor() as curs:
            curs.execute("FROM https://lsd.so |> SELECT title")
            rows = curs.fetchall()
    except Exception as e:
        GLOBAL_CONN = None
        return establish_connection()

    return GLOBAL_CONN


def run_lsd(lsd_sql):
    conn = establish_connection()
    with conn.cursor() as curs:
        curs.execute(lsd_sql)
        rows = curs.fetchall()
        return [list(r) for r in rows]
