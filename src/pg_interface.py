import psycopg2
import psycopg2.extras

connection_string = "dbname='postgres' user='danielkato'"
conn = psycopg2.connect(connection_string)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def SELECT(sql_str):
    cur.execute("SELECT " + sql_str)
    rows = cur.fetchall()
    return rows

def INSERT(sql_str, vals):
    cur = conn.cursor()
    cur.execute("INSERT " + sql_str, vals)

def CLOSE():
    conn.commit()
    cur.close()
    conn.close()
