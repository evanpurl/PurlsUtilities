import sqlite3
from sqlite3 import Error


async def sqlite_create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error or Exception as e:
        print(f"create db: {e}")


async def sqlite_create_table(conn, tabledata):
    """ create a table from the create_table_sql statement
    :param tabledata: Data to create in table
    :param conn: Connection object
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(tabledata)
        c.close()

    except Error or Exception as e:
        print(f"create table: {e}")


async def sqlite_createuniqueindex(conn, datatoinsert):
    try:
        c = conn.cursor()
        c.execute(datatoinsert)
        conn.commit()
        c.close()
        conn.close()
    except Error or Exception as e:
        print(f"createuniqueindex: {e}")


async def sqlite_run(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        c.close()

    except Error or Exception as e:
        print(f"sqlite run: {e}")


async def sqlite_get(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        option = c.fetchall()
        if not option:
            return 0
        if len(option) == 0:
            return 0
        return option
    except Error or Exception as e:
        print(f"sqlite get: {e}")
        return []
