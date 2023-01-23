import sqlite3


def connect_db(db_name: str):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def create_users_table():
    connection, cursor = connect_db("translator.db")
    sql = """
        DROP TABLE IF EXISTS users;
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            phone_number TEXT,
            telegram_id BIGINT NOT NULL UNIQUE
        );
    """

    cursor.executescript(sql)

    connection.commit()
    connection.close()


create_users_table()
