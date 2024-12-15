import sqlite3 as sql


def db_setup():
    conn = sql.connect('memo.db')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                tasks TEXT,
                note_type INT NOT NULL
            )
        ''')

    conn.commit()
    conn.close()


def select_all():
    global con, cursor
    try:
        con = sql.connect("memo.db")
        cursor = con.cursor()
        query_select_all = "SELECT * FROM notes"
        cursor.execute(query_select_all)
        return cursor.fetchall()
    except sql.DatabaseError as e:
        if con:
            con.rollback()
            print(e)
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


def add(title, content, tasks, note_type):
    global con, cursor
    try:
        con = sql.connect("memo.db")
        cursor = con.cursor()
        query_insert = "INSERT INTO notes (title, content, tasks, note_type) VALUES (?, ?, ?, ?)"
        cursor.execute(query_insert, (title, content, tasks, note_type))
        con.commit()
    except sql.DatabaseError as e:
        if con:
            con.rollback()
            print(e)
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()