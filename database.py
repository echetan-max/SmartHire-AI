import sqlite3

def connect_db():
    return sqlite3.connect("smart_hire.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS job_descriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        responsibilities TEXT,
        qualifications TEXT,
        skills TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        name TEXT,
        email TEXT,
        phone TEXT,
        education TEXT,
        experience TEXT,
        skills TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS match_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER,
        resume_id INTEGER,
        score REAL,
        FOREIGN KEY (job_id) REFERENCES job_descriptions(id),
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
    """)

    conn.commit()
    conn.close()