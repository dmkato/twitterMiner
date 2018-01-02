import psycopg2
import psycopg2.extras

class PG():
    def __init__(self):
        self.connection_string = "dbname='postgres' user='danielkato'"
        self.conn = psycopg2.connect(connection_string)
        self.cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def SELECT(sql_str):
        self.cur.execute("SELECT " + sql_str)
        rows = cur.fetchall()
        return rows

    def INSERT(sql_str, vals):
        cur.execute("INSERT " + sql_str, vals)

    def close():
        conn.commit()
        cur.close()
        conn.close()
