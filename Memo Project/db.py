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