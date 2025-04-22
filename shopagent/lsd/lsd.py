import os
import psycopg2
from time import sleep


GLOBAL_CONN = None
def establish_connection():
    global GLOBAL_CONN

    if GLOBAL_CONN is None:
        while True:
            try:
                GLOBAL_CONN = psycopg2.connect(
                    host="lsd.so",
                    database=os.environ.get("LSD_USER"),
                    user=os.environ.get("LSD_USER"),
                    password=os.environ.get("LSD_API_KEY"),
                    port="5432",
                )
                break
            except Exception as e:
                print("Ran into an issue connecting (now sleeping before trying again):", e)
                sleep(1)

    # Try out a simple request before handing back the postgres connection
    # in case, say, the wifi suddenly cut out after having already been
    # running the script a while. Yeah, not fun
    try:
        with GLOBAL_CONN.cursor() as curs:
            curs.execute("FROM https://lsd.so |> SELECT title")
            rows = curs.fetchall()
    except Exception as e:
        GLOBAL_CONN = None
        return establish_connection()

    return GLOBAL_CONN


def run_lsd(lsd_sql, retrying=False):
    conn = establish_connection()
    try:
        with conn.cursor() as curs:
            curs.execute(lsd_sql)
            rows = curs.fetchall()
            return [list(r) for r in rows]
    except Exception as e:
        if retrying:
            return []

        global GLOBAL_CONN
        GLOBAL_CONN = None
        return run_lsd(lsd_sql, True)
