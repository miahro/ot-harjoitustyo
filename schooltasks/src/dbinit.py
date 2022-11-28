from dbcon import db_connection

def create_tables(connection):

    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            user_id TEXT NOT NULL UNIQUE,
            passwd TEXT NOT NULL,
            teacher BOOLEAN);"""
           )
    connection.commit()

    cursor.execute("""CREATE TABLE Topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL UNIQUE);"""
           )
    connection.commit()

    cursor.execute("""CREATE TABLE Tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER REFERENCES Topics,
            difficulty INTEGER NOT NULL,
            question TEXT NOT NULL,
            correct TEXT NOT NULL,
            wrong1 TEXT NOT NULL,
            wrong2 TEXT NOT NULL,
            wrong3 TEXT NOT NULL);"""
    )

    connection.commit()

    cursor.execute("""CREATE TABLE Results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER REFERENCES Users,
            task_id INTEGER REFERENCES Tasks,
            result BOOLEAN);"""
    )
    connection.commit()

def delete_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Users")
    connection.commit

    cursor.execute("DROP TABLE IF EXISTS Topics")
    connection.commit

    cursor.execute("DROP TABLE IF EXISTS Tasks")
    connection.commit
    
    cursor.execute("DROP TABLE IF EXISTS Results")
    connection.commit
 

def init_db():
    connection = db_connection()
    delete_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    init_db()