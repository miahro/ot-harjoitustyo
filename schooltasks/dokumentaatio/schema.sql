CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    user_id TEXT NOT NULL UNIQUE
    passwd TEXT NOT NULL
    teacher BOOLEAN
);

CREATE TABLE Topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL UNIQUE
);

CREATE TABLE Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER REFERENCES Topics,
    difficulty INTEGER NOT NULL,
    question TEXT NOT NULL,
    correct TEXT NOT NULL,
    wrong1 TEXT NOT NULL,
    wrong2 TEXT NOT NULL,
    wrong3 TEXT NOT NULL
);

CREATE TABLE Results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER REFERENCES Users,
    task_id INTEGER REFERENCES Tasks,
    result BOOLEAN
);